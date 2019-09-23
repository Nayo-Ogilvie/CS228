import numpy as np
import pickle
import os
import time

#Add classes and variables from other python files
from pygameWindow_Del03 import PYGAME_WINDOW

class READER:
    def __init__(self):
        self.pickle_in = open("./userData/gesture0.p","rb")
        self.gestureData = pickle.load(self.pickle_in)
        self.Gesture_Count()
        self.pygameWindow = PYGAME_WINDOW()
        self.currentBone = []
        self.xBaseNotYetScaled = 0
        self.yBaseNotYetScaled = 0
        self.xTipNotYetScaled = 0
        self.yTipNotYetScaled = 0
        self.xBasePostScale = 0
        self.yBasePostScale = 0
        self.xTipPostScale = 0
        self.yTipPostScale = 0
        self.xMin = -400.0
        self.xMax = 400.0
        self.yMin = -400.0
        self.yMax = 400.0
        #print(self.gestureData)
        #self.Draw_Gestures()
        #print(self.numGestures)
        
    def Gesture_Count(self):
        path, dirs, files = next(os.walk('userData'))
        self.numGestures = len(files)
        
    def Print_Gestures(self):
        for i in range(0, self.numGestures):
            gestureString = "./userData/gesture" + str(i) + ".p"
            self.pickle_in = open(gestureString,"rb")
            self.gestureData = pickle.load(self.pickle_in)
            print(self.gestureData)
    
    def Draw_Gestures(self):
        while True:
            self.Draw_Each_Gesture_Once()
            
    def Draw_Each_Gesture_Once(self):
        for i in range(0, self.numGestures):
            gestureString = "./userData/gesture" + str(i) + ".p"
            self.pickle_in = open(gestureString,"rb")
            self.gestureData = pickle.load(self.pickle_in)
            self.Draw_Gesture(i)
            
    def Draw_Gesture(self, integer):
        self.pygameWindow.Prepare()
        for i in range(0,5):
            for j in range(0,4):
                for g in range(0,6):
                    self.currentBone.append(self.gestureData[i, j, g])
                self.xBaseNotYetScaled = self.currentBone[0]
                self.yBaseNotYetScaled = self.currentBone[2]
                self.xTipNotYetScaled = self.currentBone[3]
                self.yTipNotYetScaled = self.currentBone[5]
                self.xBasePostScale, self.yBasePostScale = self.Handle_Vector_From_Leap(self.xBaseNotYetScaled, self.yBaseNotYetScaled)
                self.xTipPostScale, self.yTipPostScale = self.Handle_Vector_From_Leap(self.xTipNotYetScaled, self.yTipNotYetScaled)
                #print("xBase: ", self.xBaseNotYetScaled)
                #print("yBase: ", self.yBaseNotYetScaled)
                #print("xTip: ", self.xTipNotYetScaled)
                #print("yTip: ", self.yTipNotYetScaled)
                #print("xBase: ", self.xBasePostScale)
                #print("yBase: ", self.yBasePostScale)
                #print("xTip: ", self.xTipPostScale)
                #print("yTip: ", self.yTipPostScale)
                self.pygameWindow.Draw_Black((0,0,255), self.xBasePostScale, self.yBasePostScale, self.xTipPostScale, self.yTipPostScale, 1)
                del self.currentBone[:]
                #YOUR ON STEP 51 figure it out
        #print(self.gestureData)
        self.pygameWindow.Reveal()
        time.sleep(1)
        
    def Scale(self, value, before_min, before_max, after_min, after_max):
        if ((before_max - before_min) <= 0):
            return 0
        #print("Before min: ", before_min)
        #print("Before max: ", before_max)
        #print("after_min: ", after_min)
        #print("after_max: ", after_max)
        #print("value: ", value)
        scaleValue = (float(value) - float(before_min)) / (float(before_max) - float(before_min))
        scaledPointValue = (scaleValue * (after_max - after_min)) + after_min
        #print(scaledPointValue)
        return int(scaledPointValue)
        
    def Handle_Vector_From_Leap(self, x, y):
        x = int(x)
        y = int(y)
        if ( x < self.xMin):
            self.xMin = x
        if ( x > self.xMax):
            self.xMax = x
        if ( y < self.yMin):
            self.yMin = y
        if ( y > self.yMax):
            self.yMax = y
        pygameX = self.Scale(x, self.xMin, self.xMax, 600, 0)
        pygameY = self.Scale(y, self.yMin, self.yMax, 0, 600)
        return pygameX, pygameY