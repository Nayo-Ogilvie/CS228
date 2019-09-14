import Leap
import random
import numpy as np

#Add classes and variables from other python files
from pygameWindow_Del03 import PYGAME_WINDOW

class DELIVERABLE:
    def __init__(self):
        self.controller = Leap.Controller()
        self.pygameWindow = PYGAME_WINDOW()
        self.x = 300
        self.y = 300
        self.xMin = 1000.0
        self.xMax = -1000.0
        self.yMin = 1000.0
        self.yMax = -1000.0
        self.currentNumberOfHands = 0
        self.previousNumberOfHands = 0
        self.Color = (0,255,0)
        self.Green = (0,255,0)
        self.Red = (255,0,0)
        self.gestureData = np.zeros((5,4,6),dtype='f')
        
    def Recording_Is_Ending(self):
        if (self.currentNumberOfHands < self.previousNumberOfHands):
            return True
        else:
            return False
        
    def Handle_Frame(self, frame):
        handList = frame.hands
        self.currentNumberOfHands = len(handList)
        if (self.currentNumberOfHands > 1):
            self.Color = self.Red
        else:
            self.Color = self.Green
        DomHand = handList[0]
        fingers = DomHand.fingers
        i = 0
        for finger in fingers:
            self.Handle_Finger(finger, i)
            i = i + 1
        if (self.Recording_Is_Ending()):
            print(self.gestureData)
            
    def Handle_Finger(self, finger, i):
        for b in range(4):
            self.Handle_Bone(finger.bone(b), i, b)
     
    def Handle_Bone(self, bone, i, j):
        tip = bone.next_joint
        base = bone.prev_joint
        if (self.Recording_Is_Ending()):
            self.gestureData[i, j, 0] = base[0]
            self.gestureData[i, j, 1] = base[1]
            self.gestureData[i, j, 2] = base[2]
            self.gestureData[i, j, 3] = tip[0]
            self.gestureData[i, j, 4] = tip[1]
            self.gestureData[i, j, 5] = tip[2]
        xTip, yTip = self.Handle_Vector_From_Leap(tip)
        xBase, yBase = self.Handle_Vector_From_Leap(base)
        #invert B so thickest is at wrist
        invertedI = (4 - j) * 2
        self.pygameWindow.Draw_Black(self.Color, xBase, yBase, xTip, yTip, invertedI)
        
    def Handle_Vector_From_Leap(self, v):
        self.x = int(v[0])
        self.y = int(v[2])
        if ( self.x < self.xMin):
            self.xMin = self.x
        if ( self.x > self.xMax):
            self.xMax = self.x
        if ( self.y < self.yMin):
            self.yMin = self.y
        if ( self.y > self.yMax):
            self.yMax = self.y
        pygameX = self.Scale(int(v[0]), self.xMin, self.xMax, 0, 600)
        pygameY = self.Scale(int(v[2]), self.yMin, self.yMax, 0, 600)
        return pygameX, pygameY
        
    def Scale(self, value, before_min, before_max, after_min, after_max):
        if ((before_max - before_min) <= 0):
            return 0
        scaleValue = (float(value) - float(before_min)) / (float(before_max) - float(before_min))
        scaledPointValue = (scaleValue * (after_max - after_min)) + after_min
        return int(scaledPointValue)
    
    def Run_Forever(self):
        while True:
            self.pygameWindow.Prepare()
            frame = self.controller.frame()
            hands = frame.hands
            if (not hands.is_empty):
                self.Handle_Frame(frame)
            self.previousNumberOfHands = self.currentNumberOfHands
            self.pygameWindow.Reveal()