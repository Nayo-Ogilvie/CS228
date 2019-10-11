import sys
#Add path to PATH
sys.path.insert(0,'../../x86')


import Leap
import random
import pickle
import numpy as np

#Add classes and variables from other python files
from pygameWindow import PYGAME_WINDOW

clf = pickle.load( open('userData/classifier.p', 'rb'))
testData = np.zeros((1,30),dtype='f')

#Variable Init
pygameWindow = PYGAME_WINDOW()
x = 300
y = 300
pygameX = 300
pygameY = 300
xMin = 1000.0
xMax = -1000.0
yMin = 1000.0
yMax = -1000.0
k = 0
oldPredicted = 0
#Initialize controller
controller = Leap.Controller()

#Function List

def Scale(value, before_min, before_max, after_min, after_max):
    if ((before_max - before_min) <= 0):
        return 0
    #print("Before min: ", before_min)
    #print("Before max: ", before_max)
    #print("value: ", value)
    scaleValue = (float(value) - float(before_min)) / (float(before_max) - float(before_min))
    scaledPointValue = (scaleValue * (after_max - after_min)) + after_min
    #print(scaledPointValue)
    return int(scaledPointValue)

def Handle_Vector_From_Leap(v):
    global x, y, xMin, xMax, yMin, yMax
    x = int(v[0])
    y = int(v[2])
    if ( x < xMin):
        xMin = x
    if ( x > xMax):
        xMax = x
    if ( y < yMin):
        yMin = y
    if ( y > yMax):
        yMax = y
    pygameX = Scale(int(v[0]), xMin, xMax, 0, 600)
    pygameY = Scale(int(v[2]), yMin, yMax, 0, 600)
    return pygameX, pygameY

def Handle_Bone(bone, i):
    global testData, k
    tip = bone.next_joint
    base = bone.prev_joint
    xTip, yTip = Handle_Vector_From_Leap(tip)
    xBase, yBase = Handle_Vector_From_Leap(base)
    #print(k)
    #invert B so thickest is at wrist
    #print(tip[0])
    #print(tip[1])
    #print(tip[2])
    if ( (i == 0) or (i == 3) ):
        testData[0,k] = tip[0]
        testData[0,k+1] = tip[1]
        testData[0,k+2] = tip[2]
        k = k + 3
    invertedI = (4 - i) * 2
    pygameWindow.Draw_Black_Line(xBase, yBase, xTip, yTip, invertedI)
    
def Handle_Finger(finger):
    for b in range(4):
        Handle_Bone(finger.bone(b), b)

def Handle_Frame (frame):
    global x, y, xMin, xMax, yMin, yMax, k, testData, oldPredicted
    hand = frame.hands[0]
    fingers = hand.fingers
    k = 0
    for finger in fingers:
        Handle_Finger(finger)
    #print("before: ", testData)
    testData = CenterData(testData)
    #print("after: ", testData)
    predictedClass = clf.Predict(testData)
    if (predictedClass != oldPredicted):
        oldPredicted = predictedClass
    return predictedClass
    
def CenterData(X):
    allXCoordinates = X[0,::3]
    meanValue = allXCoordinates.mean()
    X[0,::3] = allXCoordinates - meanValue
    allXCoordinates = X[0,1::3]
    meanValue = allXCoordinates.mean()
    X[0,1::3] = allXCoordinates - meanValue
    allXCoordinates = X[0,2::3]
    meanValue = allXCoordinates.mean()
    X[0,2::3] = allXCoordinates - meanValue
    return X
    
#Infinite Loop
while True:
    pygameWindow.Prepare()
    frame = controller.frame()
    hands = frame.hands
    text = " "
    if (not hands.is_empty):
        text = Handle_Frame(frame)
        
    pygameWindow.Update_Text(str(text))
    pygameWindow.Reveal()


print(pygameWindow)