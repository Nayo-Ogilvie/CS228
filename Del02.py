import sys
#Add path to PATH
sys.path.insert(0,'../x86')


import Leap
import random

#Add classes and variables from other python files
from pygameWindow import PYGAME_WINDOW


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

#Initialize controller
controller = Leap.Controller()

#Function List
def Perturb_Circle_Position():
    global x, y
    fourSidedDieRoll = random.randint(1,4)
    if (fourSidedDieRoll == 1):
        x-=2
    elif (fourSidedDieRoll == 2):
        x+=2
    elif (fourSidedDieRoll == 3):
        y-=2
    elif (fourSidedDieRoll == 4):
        y+=2

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
    tip = bone.next_joint
    base = bone.prev_joint
    xTip, yTip = Handle_Vector_From_Leap(tip)
    xBase, yBase = Handle_Vector_From_Leap(base)
    #invert B so thickest is at wrist
    invertedI = (4 - i) * 2
    pygameWindow.Draw_Black_Line(xBase, yBase, xTip, yTip, invertedI)
    
def Handle_Finger(finger):
    for b in range(4):
        Handle_Bone(finger.bone(b), b)

def Handle_Frame (frame):
    global x, y, xMin, xMax, yMin, yMax
    hand = frame.hands[0]
    fingers = hand.fingers
    for finger in fingers:
        Handle_Finger(finger)
        #print(finger)
    #Leaving as 1 since that is the integer map and class can't be founds
    #indexFingerList = fingers.finger_type(1)
    #indexFinger = indexFingerList[0]
    #Same as above making 3 
    #distalPhalanx = indexFinger.bone(3)
    #tip = distalPhalanx.next_joint
    #x = int(tip[0])
    #y = int(tip[1])
    #if ( x < xMin):
    #    xMin = x
    #if ( x > xMax):
    #    xMax = x
    #if ( y < yMin):
    #    yMin = y
    #if ( y > yMax):
    #    yMax = y
    #print("xMin: ", xMin)
    #print("xMax: ", xMax)
    #print("yMin: ", yMin)
    #print("yMax: ", yMax)
    #print(tip)
    #print(hand)
    
#Infinite Loop
while True:
    #print('Draw Something.')
    #print(frame)
    pygameWindow.Prepare()
    frame = controller.frame()
    hands = frame.hands
    if (not hands.is_empty):
        #print("hand detected.")
        Handle_Frame(frame)
        #pygameX = Scale(x, xMin, xMax, 0, 600)
        #pygameY = Scale(y, yMin, yMax, 600, 0)
    #pygameWindow.Draw_Black_Circle(pygameX,pygameY)
    #pygameWindow.Draw_Black_Circle(x,y)
    #Perturb_Circle_Position()
    pygameWindow.Reveal()


print(pygameWindow)