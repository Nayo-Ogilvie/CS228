import sys
#Add path to PATH
sys.path.insert(0,'../../x86')


import Leap
import time
import random
import pickle
import numpy as np

#Add classes and variables from other python files
from pygameWindow import PYGAME_WINDOW

clf = pickle.load( open('userData/classifier.p', 'rb'))
testData = np.zeros((1,30),dtype='f')

#Deliverable 8 stuff
database = pickle.load(open('userData/database.p', 'rb'))

sys.stdout.flush()
userName = raw_input('Please enter your name: ')
if userName in database:
    print('Welcome back ' + userName + '.')
    database[userName]['logins'] = database[userName]['logins'] + 1
else:
    database[userName] = {}
    database[userName]['logins'] = 1
    print('Welcome ' + userName + '.')

userRecord = database[userName]

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
programState = 0
predicted_count = 0
number_generated = True
random_number = random.randint(0,9)
#show this number is attempted again
attemptString = 'digit' + str(random_number) + 'attempted'
if (attemptString in userRecord.keys()):
    userRecord[attemptString] = userRecord[attemptString] + 1
else:
    userRecord[attemptString] = 1
database[userName] = userRecord
pickle.dump(database,open('userData/database.p', 'wb'))
imagePath = "./userMoveHand.jpg"
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
    pygameX = Scale(int(v[0]), xMin, xMax, 0, pygameWindow.pygameWindowWidth/2)
    pygameY = Scale(int(v[2]), yMin, yMax, 0, pygameWindow.pygameWindowWidth/2)
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
    testData = CenterData(testData)
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
    
def HandleState0():
    global programState, random_number, userRecord, attemptString
    pygameWindow.Prepare()
    frame = controller.frame()
    pygameWindow.Show_Image("./userMoveHand.jpg")
    #text = "Should be more"
    pygameWindow.Update_Text("Attemp Sign " + str(random_number) + ": " + str(userRecord[attemptString]))
    hands = frame.hands
    if (not hands.is_empty):
        programState = 1
    pygameWindow.Reveal()
        
def HandleState1():
    global programState, imagePath, random_number, userRecord, attemptString
    pygameWindow.Prepare()
    frame = controller.frame()
    hands = frame.hands
    centered(frame, random_number)
    #text = "Not Centered"
    pygameWindow.Show_Image(imagePath)
    pygameWindow.Update_Text("Attemp Sign " + str(random_number) + ": " + str(userRecord[attemptString]))
    if (number_generated):
        pygameWindow.Show_Image_Lower("./asl_" + str(random_number) + ".jpg")
    #text = Handle_Frame(frame)
    Handle_Frame(frame)
    #pygameWindow.Hide_Startup_Graphic()
    pygameWindow.Reveal()
    if (hands.is_empty):
        programState = 0
    if (centered(frame, random_number)):
        programState = 2
        
def HandleState2():
    global programState, imagePath, predicted_count, number_generated, random_number, userRecord, attemptString, userName
    if (not number_generated):
        #generate random number
        random_number = random.randint(0,9)
        pygameWindow.Show_Image_Lower("./asl_" + str(random_number) + ".jpg")
        #show this number is attempted again
        attemptString = 'digit' + str(random_number) + 'attempted'
        if (attemptString in userRecord.keys()):
            userRecord[attemptString] = userRecord[attemptString] + 1
        else:
            userRecord[attemptString] = 1
        database[userName] = userRecord
        pickle.dump(database,open('userData/database.p', 'wb'))
        number_generated = True
    pygameWindow.Prepare()
    frame = controller.frame()
    hands = frame.hands
    #text = "Centered"
    pygameWindow.Show_Image(imagePath)
    pygameWindow.Update_Text("Attemp Sign " + str(random_number) + ": " + str(userRecord[attemptString]))
    pygameWindow.Show_Image_Lower("./asl_" + str(random_number) + ".jpg")
    predicted = Handle_Frame(frame)
    #pygameWindow.Update_Text(str(text))
    pygameWindow.Reveal()
    if (predicted == random_number):
        predicted_count = predicted_count + 1
    if (hands.is_empty):
        programState = 0
        predicted_count = 0
    elif (not centered(frame, random_number)):
        programState = 1
        predicted_count = 0
    elif (predicted_count == 10):
        programState = 3
        
def HandleState3():
    global programState, predicted_count, number_generated, random_number, userRecord, attemptString
    pygameWindow.Prepare()
    frame = controller.frame()
    hands = frame.hands
    #text = "Centered"
    pygameWindow.Show_Image("./checkMark.png")
    pygameWindow.Show_Image_Lower("./asl_" + str(random_number) + ".jpg")
    pygameWindow.Update_Text("Attemp Sign " + str(random_number) + ": " + str(userRecord[attemptString]))
    #predicted = Handle_Frame(frame)
    #pygameWindow.Update_Text(str(text))
    pygameWindow.Reveal()
    time.sleep(4)
    predicted_count = 0
    number_generated = False
    if (hands.is_empty):
        programState = 0
    elif (not centered(frame, random_number)):
        programState = 1
    else:
        programState = 2
        
def centered(frame, random_number):
    global imagePath
    hand = frame.hands[0]
    fingers = hand.fingers
    centerLoc = fingers[2].bone(0).next_joint
    #print(centerLoc)
    if (-100 < centerLoc[0] < 100):
        if (150 < centerLoc[1] < 250):
            if (-50 < centerLoc[2] < 50):
                pygameWindow.Show_Image("./helpful_" + str(random_number) + ".jpg")
                imagePath = "./helpful_" + str(random_number) + ".jpg"
                pygameWindow.Show_Image_Lower("./asl_" + str(random_number) + ".jpg")
                #imagePath = "./asl_5.jpg"
                return True
            elif(centerLoc[2] < -50):
                pygameWindow.Show_Image("./userMoveHand_backward.jpg")
                imagePath = "./userMoveHand_backward.jpg"
            elif(centerLoc[2] > 50):
                pygameWindow.Show_Image("./userMoveHand_forward.jpg")
                imagePath = "./userMoveHand_forward.jpg"
        elif(centerLoc[1] > 250):
            pygameWindow.Show_Image("./userMoveHand_down.jpg")
            imagePath = "./userMoveHand_down.jpg"
        elif(centerLoc[1] < 150):
            pygameWindow.Show_Image("./userMoveHand_up_Final.jpg")
            imagePath = "./userMoveHand_up_Final.jpg"
    elif(centerLoc[0] > 100):
        pygameWindow.Show_Image("./userMoveHand_left.jpg")
        imagePath = "./userMoveHand_left.jpg"
    elif(centerLoc[0] < -100):
        pygameWindow.Show_Image("./userMoveHand_right.jpg")
        imagePath = "./userMoveHand_right.jpg"
    return False

print(database)
    
#Infinite Loop
while True:
    if (programState == 0):
        HandleState0()
    elif (programState == 1):
        HandleState1()
    elif (programState == 2):
        HandleState2()
    elif (programState == 3):
        HandleState3()


print(pygameWindow)