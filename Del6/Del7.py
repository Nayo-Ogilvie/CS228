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
    #0
    database[userName]['0'] = {}
    database[userName]['0']['active_time'] = 0
    database[userName]['0']['correct'] = 0
    database[userName]['0']['incorrect'] = 0
    database[userName]['0']['attempts'] = 0
    database[userName]['0']['level'] = 0
    database[userName]['0']['previous_num'] = False
    #1
    database[userName]['1'] = {}
    database[userName]['1']['active_time'] = 0
    database[userName]['1']['correct'] = 0
    database[userName]['1']['incorrect'] = 0
    database[userName]['1']['attempts'] = 0
    database[userName]['1']['level'] = 0
    database[userName]['1']['previous_num'] = False
    #2
    database[userName]['2'] = {}
    database[userName]['2']['active_time'] = 0
    database[userName]['2']['correct'] = 0
    database[userName]['2']['incorrect'] = 0
    database[userName]['2']['attempts'] = 0
    database[userName]['2']['level'] = 0
    database[userName]['2']['previous_num'] = False
    #3
    database[userName]['3'] = {}
    database[userName]['3']['active_time'] = 0
    database[userName]['3']['correct'] = 0
    database[userName]['3']['incorrect'] = 0
    database[userName]['3']['attempts'] = 0
    database[userName]['3']['level'] = 0
    database[userName]['3']['previous_num'] = False
    #4
    database[userName]['4'] = {}
    database[userName]['4']['active_time'] = 0
    database[userName]['4']['correct'] = 0
    database[userName]['4']['incorrect'] = 0
    database[userName]['4']['attempts'] = 0
    database[userName]['4']['level'] = 0
    database[userName]['4']['previous_num'] = False
    #5
    database[userName]['5'] = {}
    database[userName]['5']['active_time'] = 0
    database[userName]['5']['correct'] = 0
    database[userName]['5']['incorrect'] = 0
    database[userName]['5']['attempts'] = 0
    database[userName]['5']['level'] = 0
    database[userName]['5']['previous_num'] = False
    #6
    database[userName]['6'] = {}
    database[userName]['6']['active_time'] = 0
    database[userName]['6']['correct'] = 0
    database[userName]['6']['incorrect'] = 0
    database[userName]['6']['attempts'] = 0
    database[userName]['6']['level'] = 0
    database[userName]['6']['previous_num'] = False
    #7
    database[userName]['7'] = {}
    database[userName]['7']['active_time'] = 0
    database[userName]['7']['correct'] = 0
    database[userName]['7']['incorrect'] = 0
    database[userName]['7']['attempts'] = 0
    database[userName]['7']['level'] = 0
    database[userName]['7']['previous_num'] = False
    #8
    database[userName]['8'] = {}
    database[userName]['8']['active_time'] = 0
    database[userName]['8']['correct'] = 0
    database[userName]['8']['incorrect'] = 0
    database[userName]['8']['attempts'] = 0
    database[userName]['8']['level'] = 0
    database[userName]['8']['previous_num'] = False
    #9
    database[userName]['9'] = {}
    database[userName]['9']['active_time'] = 0
    database[userName]['9']['correct'] = 0
    database[userName]['9']['incorrect'] = 0
    database[userName]['9']['attempts'] = 0
    database[userName]['9']['level'] = 0
    database[userName]['9']['previous_num'] = False
    print('Welcome ' + userName + '.')

userRecord = database[userName]
#setup previous num to be False for all
for value in range(10):
    if (userRecord[str(value)]['previous_num']):
        userRecord[str(value)]['previous_num'] = False
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
programState = 6
predicted_count = 0
wrong_predicted_count = 0
lastPredicted = 0
number_generated = True
time_start = time.time()
random_number = random.randint(0,9)
#get overall status amount
overallTotalAttemptsStart = 0
overallCorrectStart = 0
numberSlotArray = [0,0,0,0,0,0,0,0,0]
filled_value =  np.zeros(9)
#filled_value = filled_value.reshape(3,3)
for userValues in database.keys():
    print(userValues)
    for number in range(10):
        print(number)
        overallTotalAttemptsStart = overallTotalAttemptsStart + database[userValues][str(number)]['correct'] + database[userValues][str(number)]['incorrect']
        overallCorrectStart = overallCorrectStart + database[userValues][str(number)]['correct']
if(overallTotalAttemptsStart != 0):
    overallPercentRightStart = float(overallCorrectStart) / overallTotalAttemptsStart
else:
    overallPercentRightStart = 0
print("overall percent: " + str(overallPercentRightStart))
#get amount for individual user
totalAttemptsStart = 0
correctStart = 0
for number in range(10):
    print(number)
    totalAttemptsStart = totalAttemptsStart + userRecord[str(number)]['correct'] + userRecord[str(number)]['incorrect']
    correctStart = correctStart + userRecord[str(number)]['correct']
totalAttemptsNow = 0
correctNow = 0
if (totalAttemptsStart != 0):
    percentRightStart = float(correctStart) / totalAttemptsStart
else:
    percentRightStart = 0
print("user percent: " + str(percentRightStart))
percentRightNow = 0.0
timer_value = 10
database[userName][str(random_number)]['previous_num'] = True
level = database[userName][str(random_number)]['level']
#show this number is attempted again
#attemptString = 'digit' + str(random_number) + 'attempted'
#if (attemptString in userRecord.keys()):
#    userRecord[attemptString] = userRecord[attemptString] + 1
#else:
#    userRecord[attemptString] = 1
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
    
def Handle_Bone_Tik(bone, i):
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
    #pygameWindow.Draw_Black_Line(xBase, yBase, xTip, yTip, invertedI)
    
def Handle_Finger_Tik(finger):
    for b in range(4):
        Handle_Bone_Tik(finger.bone(b), b)

def Handle_Frame_Tik(frame):
    global x, y, xMin, xMax, yMin, yMax, k, testData, oldPredicted
    hand = frame.hands[0]
    fingers = hand.fingers
    k = 0
    for finger in fingers:
        Handle_Finger_Tik(finger)
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

def HandleStateA():
    global programState
    pygameWindow.Prepare()
    programState = pygameWindow.displayOpenningWindow()
    pygameWindow.Reveal()

def HandleState0():
    global programState, random_number, userRecord, attemptString, time_start, percentRightStart, percentRightNow, overallPercentRightStart
    #print(userRecord)
    pygameWindow.Prepare()
    frame = controller.frame()
    pygameWindow.Show_Image("./userMoveHand.jpg")
    pygameWindow.Draw_Progress_Bar(overallPercentRightStart, percentRightStart,percentRightNow)
    if (pygameWindow.MenuButton()):
        programState = 6
    time_start = time.time()
    #text = "Should be more"
    #pygameWindow.Update_Text("Attemp Sign " + str(random_number) + ": " + str(userRecord[str(random_number)]['attempts']))
    #pygameWindow.Update_Text_Timer("Timer: " + str(int(timer_value - (time.time() - time_start))))
    hands = frame.hands
    if (not hands.is_empty):
        programState = 1
    pygameWindow.Reveal()
        
def HandleState1():
    global programState, imagePath, random_number, userRecord, attemptString, time_start, level, percentRightStart, percentRightNow, overallPercentRightStart
    pygameWindow.Prepare()
    pygameWindow.Draw_Progress_Bar(overallPercentRightStart, percentRightStart,percentRightNow)
    frame = controller.frame()
    hands = frame.hands
    centered(frame, random_number)
    #text = "Not Centered"
    pygameWindow.Show_Image(imagePath)
    pygameWindow.Update_Text("Attemp Sign " + str(random_number) + ": " + str(userRecord[str(random_number)]['attempts']))
    pygameWindow.Update_Text_Level("Level: " + str(userRecord[str(random_number)]['level']))
    if (level == 0):
        pygameWindow.Show_Image(imagePath)
        #pygameWindow.Update_Text("Attemp Sign " + str(random_number) + ": " + str(userRecord[str(random_number)]['attempts']))
        #pygameWindow.Update_Text_Level("Level: " + str(userRecord[str(random_number)]['level']))
        pygameWindow.Show_Image_Lower("./asl_" + str(random_number) + ".jpg")
        predicted = Handle_Frame(frame)
    elif (level == 1):
        pygameWindow.Show_Image(imagePath)
        #pygameWindow.Update_Text("Attemp Sign " + str(random_number) + ": " + str(userRecord[str(random_number)]['attempts']))
        #pygameWindow.Update_Text_Level("Level: " + str(userRecord[str(random_number)]['level']))
        if ((time.time() - time_start) > 4):
            pygameWindow.Update_Text_Big(str(random_number))
        else:
            pygameWindow.Show_Image_Lower("./asl_" + str(random_number) + ".jpg")
            pygameWindow.Update_Text_Big("")
        predicted = Handle_Frame(frame)
    elif (level == 2):
        pygameWindow.Show_Image(imagePath)
        #pygameWindow.Update_Text("Attemp Sign " + str(random_number) + ": " + str(userRecord[str(random_number)]['attempts']))
        #pygameWindow.Update_Text_Level("Level: " + str(userRecord[str(random_number)]['level']))
        if ((time.time() - time_start) > 2):
            pygameWindow.Update_Text_Big(str(random_number))
        else:
            pygameWindow.Show_Image_Lower("./asl_" + str(random_number) + ".jpg")
            pygameWindow.Update_Text_Big("")
        predicted = Handle_Frame(frame)
    elif (level == 3):
        pygameWindow.Show_Image(imagePath)
        #pygameWindow.Update_Text("Attemp Sign " + str(random_number) + ": " + str(userRecord[str(random_number)]['attempts']))
        #pygameWindow.Update_Text_Level("Level: " + str(userRecord[str(random_number)]['level']))
        if ((time.time() - time_start) > 1):
            pygameWindow.Update_Text_Big(str(random_number))
        else:
            pygameWindow.Show_Image_Lower("./asl_" + str(random_number) + ".jpg")
            pygameWindow.Update_Text_Big("")
        predicted = Handle_Frame(frame)
    elif (level >= 4):
        #pygameWindow.Update_Text("Attemp Sign " + str(random_number) + ": " + str(userRecord[str(random_number)]['attempts']))
        #pygameWindow.Update_Text_Level("Level: " + str(userRecord[str(random_number)]['level']))
        pygameWindow.Update_Text_Big(str(random_number))
        #pygameWindow.Update_Text_Upper(str(random_number))
        pygameWindow.Update_Text_Timer("Timer: " + str(int(timer_value - (time.time() - time_start))))
        predicted = Handle_Frame(frame)
        #pygameWindow.Show_Image_Lower("./asl_" + str(random_number) + ".jpg")
    #text = Handle_Frame(frame)
    Handle_Frame(frame)
    #pygameWindow.Hide_Startup_Graphic()
    pygameWindow.Reveal()
    if (hands.is_empty):
        programState = 0
    if (centered(frame, random_number)):
        programState = 2
        
def HandleState2():
    global programState, imagePath, predicted_count, wrong_predicted_count, number_generated, random_number, userRecord, attemptString, userName, lastPredicted, time_start, level, timer_value, percentRightStart, percentRightNow, overallPercentRightStart
    if (not number_generated):
        #generate random number
        #random_number = random.randint(0,9)
        random_number = pickNumberPhase1()
        time_start = time.time()
        pygameWindow.Show_Image_Lower("./asl_" + str(random_number) + ".jpg")
        userRecord[str(random_number)]['attempts'] = userRecord[str(random_number)]['attempts'] + 1
        level = userRecord[str(random_number)]['level']
        #show this number is attempted again
        #attemptString = 'digit' + str(random_number) + 'attempted'
        #if (attemptString in userRecord.keys()):
        #    userRecord[attemptString] = userRecord[attemptString] + 1
        #else:
        #    userRecord[attemptString] = 1
        database[userName] = userRecord
        pickle.dump(database,open('userData/database.p', 'wb'))
        number_generated = True
    pygameWindow.Prepare()
    frame = controller.frame()
    hands = frame.hands
    #text = "Centered"
    if (level == 0):
        pygameWindow.Show_Image(imagePath)
        pygameWindow.Update_Text("Attemp Sign " + str(random_number) + ": " + str(userRecord[str(random_number)]['attempts']))
        pygameWindow.Update_Text_Level("Level: " + str(userRecord[str(random_number)]['level']))
        pygameWindow.Show_Image_Lower("./asl_" + str(random_number) + ".jpg")
        predicted = Handle_Frame(frame)
    elif (level == 1):
        pygameWindow.Update_Text("Attemp Sign " + str(random_number) + ": " + str(userRecord[str(random_number)]['attempts']))
        pygameWindow.Update_Text_Level("Level: " + str(userRecord[str(random_number)]['level']))
        if ((time.time() - time_start) > 4):
            pygameWindow.Update_Text_Big(str(random_number))
            pygameWindow.Update_Text_Upper(str(random_number))
        else:
            pygameWindow.Show_Image_Lower("./asl_" + str(random_number) + ".jpg")
            pygameWindow.Show_Image(imagePath)
            pygameWindow.Update_Text_Big("")
        predicted = Handle_Frame(frame)
    elif (level == 2):
        #pygameWindow.Show_Image(imagePath)
        pygameWindow.Update_Text("Attemp Sign " + str(random_number) + ": " + str(userRecord[str(random_number)]['attempts']))
        pygameWindow.Update_Text_Level("Level: " + str(userRecord[str(random_number)]['level']))
        if ((time.time() - time_start) > 2):
            pygameWindow.Update_Text_Big(str(random_number))
            pygameWindow.Update_Text_Upper(str(random_number))
        else:
            pygameWindow.Show_Image_Lower("./asl_" + str(random_number) + ".jpg")
            pygameWindow.Show_Image(imagePath)
            pygameWindow.Update_Text_Big("")
        predicted = Handle_Frame(frame)
    elif (level == 3):
        #pygameWindow.Show_Image(imagePath)
        pygameWindow.Update_Text("Attemp Sign " + str(random_number) + ": " + str(userRecord[str(random_number)]['attempts']))
        pygameWindow.Update_Text_Level("Level: " + str(userRecord[str(random_number)]['level']))
        if ((time.time() - time_start) > 1):
            pygameWindow.Update_Text_Big(str(random_number))
            pygameWindow.Update_Text_Upper(str(random_number))
        else:
            pygameWindow.Show_Image_Lower("./asl_" + str(random_number) + ".jpg")
            pygameWindow.Show_Image(imagePath)
            pygameWindow.Update_Text_Big("")
        predicted = Handle_Frame(frame)
    elif (level >= 4):
        pygameWindow.Update_Text("Attemp Sign " + str(random_number) + ": " + str(userRecord[str(random_number)]['attempts']))
        pygameWindow.Update_Text_Level("Level: " + str(userRecord[str(random_number)]['level']))
        pygameWindow.Update_Text_Big(str(random_number))
        pygameWindow.Update_Text_Upper(str(random_number))
        pygameWindow.Update_Text_Timer("Timer: " + str(int(timer_value - (time.time() - time_start))))
        predicted = Handle_Frame(frame)
    #pygameWindow.Update_Text(str(text))
    pygameWindow.Draw_Progress_Bar(overallPercentRightStart, percentRightStart,percentRightNow)
    pygameWindow.Draw_Hot_Cold_Bar(predicted_count, wrong_predicted_count)
    pygameWindow.Reveal()
    if (predicted == random_number):
        predicted_count = predicted_count + 1
        wrong_predicted_count = 0
    elif (predicted != random_number and predicted == lastPredicted):
        wrong_predicted_count = wrong_predicted_count + 1
        predicted_count = 0
    else:
        wrong_predicted_count = 0
        lastPredicted = predicted
    if (hands.is_empty):
        programState = 0
        predicted_count = 0
    elif (not centered(frame, random_number)):
        programState = 1
        predicted_count = 0
    elif (predicted_count == 10):
        programState = 3
    elif ( 0 <= level <= 4 and wrong_predicted_count == 30):
        programState = 4
    elif (level >= 4 and (timer_value - (time.time() - time_start)) < 0):
        programState = 4
        
def HandleState3():
    global programState, predicted_count, number_generated, random_number, userRecord, attemptString, time_start, percentRightStart, percentRightNow, totalAttemptsNow, correctNow, overallPercentRightStart
    pygameWindow.Prepare()
    frame = controller.frame()
    hands = frame.hands
    totalAttemptsNow = totalAttemptsNow + 1
    correctNow = correctNow + 1
    percentRightNow = float(correctNow) / totalAttemptsNow
    #text = "Centered"
    #Update correct Count 
    userRecord[str(random_number)]['correct'] = userRecord[str(random_number)]['correct'] + 1
    userRecord[str(random_number)]['active_time'] = userRecord[str(random_number)]['active_time'] + (time.time() - time_start )
    pygameWindow.Show_Image("./checkMark.png")
    pygameWindow.Show_Image_Lower("./asl_" + str(random_number) + ".jpg")
    pygameWindow.Update_Text("Attemp Sign " + str(random_number) + ": " + str(userRecord[str(random_number)]['attempts']))
    pygameWindow.Update_Text_Level("Level: " + str(userRecord[str(random_number)]['level']))
    pygameWindow.Draw_Progress_Bar(overallPercentRightStart,percentRightStart,percentRightNow)
    #predicted = Handle_Frame(frame)
    #pygameWindow.Update_Text(str(text))
    pygameWindow.Reveal()
    time.sleep(4)
    predicted_count = 0
    number_generated = False
    #time_start = time.time()
    if (hands.is_empty):
        programState = 0
    elif (not centered(frame, random_number)):
        programState = 1
    else:
        programState = 2
        
def HandleState4():
    global programState, predicted_count, number_generated, random_number, userRecord, attemptString, time_start, percentRightStart, percentRightNow, totalAttemptsNow, correctNow, overallPercentRightStart
    pygameWindow.Prepare()
    frame = controller.frame()
    hands = frame.hands
    totalAttemptsNow = totalAttemptsNow + 1
    percentRightNow = float(correctNow) / totalAttemptsNow
    #text = "Centered"
    #Update incorrect Count 
    userRecord[str(random_number)]['incorrect'] = userRecord[str(random_number)]['incorrect'] + 1
    userRecord[str(random_number)]['active_time'] = userRecord[str(random_number)]['active_time'] + (time.time() - time_start )
    pygameWindow.Show_Image("./incorrect.png")
    pygameWindow.Show_Image_Lower("./asl_" + str(random_number) + ".jpg")
    pygameWindow.Update_Text("Attemp Sign " + str(random_number) + ": " + str(userRecord[str(random_number)]['attempts']))
    pygameWindow.Update_Text_Level("Level: " + str(userRecord[str(random_number)]['level']))
    pygameWindow.Draw_Progress_Bar(overallPercentRightStart, percentRightStart,percentRightNow)
    #predicted = Handle_Frame(frame)
    #pygameWindow.Update_Text(str(text))
    pygameWindow.Reveal()
    time.sleep(4)
    predicted_count = 0
    number_generated = False
    #time_start = time.time()
    if (hands.is_empty):
        programState = 0
    elif (not centered(frame, random_number)):
        programState = 1
    else:
        programState = 2

def HandleState5():
    global programState, filled_value, lastPredicted, predicted_count, numberSlotArray
    winner = checkGrid(filled_value)
    if (checkTie(filled_value)):
        Restart_Game(0)
    if (winner == 1):
        Restart_Game(winner)
    elif ( winner == 2):
        Restart_Game(winner)
    print("winner: ", str(winner))
    pygameWindow.Prepare()
    print(filled_value)
    numberSlotArray = pygameWindow.diplayTikTacToe(filled_value, numberSlotArray)
    #got through filled values that can't be added
    count = 0
    taken_numbers = set()
    for item in filled_value:
        if (item != 0):
            taken_numbers.add(numberSlotArray[count])
        count = count + 1
    set_length = len(taken_numbers)
    pygameWindow.Draw_Hot_Cold_Bar_Tik(predicted_count)
    frame = controller.frame()
    hands = frame.hands
    predicted = Handle_Frame_Tik(frame)
    if (pygameWindow.MenuButton()):
        programState = 6
    pygameWindow.Reveal()
    taken_numbers.add(predicted)
    tmp_set_length = len(taken_numbers)
    if (predicted == lastPredicted and tmp_set_length != set_length):
        predicted_count = predicted_count + 1
    else:
        predicted_count = 0
        lastPredicted = predicted
    #Update the predicted count bar..
    
    
    #not centered stuff
    if (hands.is_empty):
        #Print Line Not Centered
        print("No Hands")
        predicted_count = 0
    elif (not centered(frame, random_number)):
        #Print not centered stuff maybe if time add pics
        print("Not Centered")
        predicted_count = 0
    elif (predicted_count == 10):
        #Fill Spot with an X = 1
        for item in numberSlotArray:
            print("Number in spot: " + str(item))
            if (item == predicted):
                index_X = numberSlotArray.index(predicted)
                filled_value[index_X] = 1
        winner = checkGrid(filled_value)
        if (winner == 1):
            Restart_Game(winner)
        elif ( winner == 2):
            Restart_Game(winner)
        #Wait random amount between 1-4 seconds fill spot with O = 2
        time.sleep(random.randint(1,4))
        index_O = random.randint(0,8)
        filled = filled_value[index_O]
        O_count = 0
        O_Found = False
        if (filled != 0):
            while(filled != 0):
                index_O = random.randint(0,8)
                filled = filled_value[index_O]
                O_count = O_count + 1
                if (O_count > 200):
                    for i in range(0,8):
                        filled = filled_value[i]
                        if (filled == 0):
                            index_O = i
                            O_Found = True
                            break
                    if (O_Found == False):
                        Restart_Game(0)
                    break
        filled_value[index_O] = 2
    print("Filled Value")
    print(filled_value)
    #Check Winner Before and After!
    winner = checkGrid(filled_value)
    if (winner == 1):
        Restart_Game(winner)
    elif ( winner == 2):
        Restart_Game(winner)
    print("winner: ", str(winner))
    
    #if (pygameWindow.MenuButton()):
    #    programState = 6

def Restart_Game(Winner):
    global programState, filled_value, lastPredicted, predicted_count, numberSlotArray
    #Annouce the winner
    pygameWindow.Prepare()
    if (pygameWindow.MenuButton()):
        programState = 6
    print(filled_value)
    numberSlotArray = pygameWindow.diplayTikTacToe(filled_value, numberSlotArray)
    pygameWindow.Show_winner(Winner)
    frame = controller.frame()
    hands = frame.hands
    predicted = Handle_Frame_Tik(frame)
    pygameWindow.Reveal()
    time.sleep(6)
    #Reset everything after 5 seconds
    programState = 5
    filled_value = np.zeros(9)
    lastPredicted = 0
    predicted_count = 0
    numberSlotArray = [0,0,0,0,0,0,0,0,0]
    pygameWindow.set_user_signed(True)
    

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

def pickNumberPhase1():
    global userRecord, timer_value
    #adjust for current min (need to print to find out)
    currentMin = sys.maxint
    workOnThese = []
    #Check if all digits present
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for value in range(10):
        if (userRecord[str(value)]['previous_num']):
            digits.remove(value)
            userRecord[str(value)]['previous_num'] = False
    for digit in digits:
        correct = userRecord[str(digit)]['correct']
        incorrect = userRecord[str(digit)]['incorrect']
        score = correct - incorrect
        print("Digit: " + str(digit))
        print("Score: " + str(score))
        if (score <= 0):
            userRecord[str(digit)]['level'] = 0
        if (4 > score > 0):
            userRecord[str(digit)]['level'] = score
        if (score >= 4):
            userRecord[str(digit)]['level'] = score
            timer_value = 14 - score
        if (score < currentMin):
            workOnThese = [digit]
            currentMin = score
        elif (score == currentMin):
            workOnThese.append(digit)
            #if (str(digit) in record):
            #    print("Already seen " + str(digit))
            #    digits.remove(digit)
    #check which is minimum if all digits present
    #if (len(digits) == 0):
    #    for record in userRecord.keys():
    #        if ("digit" in record):
    #            correctSign = userRecord[record]
    #            if (correctSign == currentMin):
    #                workOnThese.append(record)
    #            elif (correctSign < currentMin):
    #                currentMin = correctSign
    #                workOnThese = [record]
    #select a random number from the ones that aren't correctSign
        #digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        #tmpDigits = []
        #print(workOnThese)
        #for items in workOnThese:
        #    for digit in digits:
        #        if (str(digit) in items):
        #            tmpDigits.append(digit)
        #digits = tmpDigits
    print("Work on these:")
    print(workOnThese)
    nextItem = random.choice(workOnThese)
    print(nextItem)
    userRecord[str(nextItem)]['previous_num'] = True
    return nextItem
    
def checkGrid(grid):
    grid = np.array(grid)
    grid = grid.reshape(3,3)
    print("Grid is..")
    print(grid)
	# rows
    for x in range(0,3):
        row = set([grid[x][0],grid[x][1],grid[x][2]])
        print("Row")
        print(x)
        print(row)
        if (len(row) == 1 and grid[x][0] != 0):
            return grid[x][0]
	# columns
    for y in range(0,3):
        column = set([grid[0][y],grid[1][y],grid[2][y]])
        print("Column")
        print(y)
        print(column)
        if (len(column) == 1 and grid[0][y] != 0):
            return grid[0][y]
    # diagonals
    diag1 = set([grid[0][0],grid[1][1],grid[2][2]])
    diag2 = set([grid[0][2],grid[1][1],grid[2][0]])
    if len(diag1) == 1 or len(diag2) == 1 and grid[1][1] != 0:
        return grid[1][1]
    return 0

def checkTie(grid):
    for item in grid:
        if item == 0:
            return False
    return True

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
    elif (programState == 4):
        HandleState4()
    elif (programState == 5):
        HandleState5()
    elif (programState == 6):
        HandleStateA()

print(pygameWindow)