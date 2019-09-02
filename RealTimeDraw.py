from pygameWindow import PYGAME_WINDOW
import random

#Variable Init
pygameWindow = PYGAME_WINDOW()
x = 300
y = 300

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
        

#Infinite Loop
while True:
    #print('Draw Something.')
    pygameWindow.Prepare()
    pygameWindow.Draw_Black_Circle(x,y)
    Perturb_Circle_Position()
    pygameWindow.Reveal()


print(pygameWindow)