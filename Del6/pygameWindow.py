import pygame
import constants
import os
import sys


class PYGAME_WINDOW:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((constants.pygameWindowWidth,constants.pygameWindowDepth))
        pygame.font.init()
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)
        self.bigfont = pygame.font.SysFont('Comic Sans MS', 100)
        self.pygameWindowWidth = constants.pygameWindowWidth
        self.pygameWindowDepth = constants.pygameWindowDepth
        self.startup_image = pygame.image.load(os.path.join('./userMoveHand.jpg'))
        
    def Prepare(self):
        pygame.event.get()
        self.screen.fill((255,255,255))
        
    def Reveal(self):
        pygame.display.update()
        
    def Update_Text(self, text):
        textsurface = self.myfont.render(text, False, (0, 0, 0))
        self.screen.blit(textsurface,(0,550))
        
    def Update_Text_Level(self, text):
        textsurface = self.myfont.render(text, False, (0, 0, 0))
        self.screen.blit(textsurface,(0,500))
        
    def Update_Text_Big(self, text):
        textsurface = self.bigfont.render(text, False, (0, 0, 0))
        self.screen.blit(textsurface,(400,400))
        
    def Update_Text_Upper(self, text):
        textsurface = self.bigfont.render(text, False, (0, 0, 0))
        self.screen.blit(textsurface,(400,100))
    
    def Update_Text_Timer(self, text):
        textsurface = self.myfont.render(text, False, (0, 0, 0))
        self.screen.blit(textsurface,(0,470))
        
    def Draw_Black_Circle(self,x,y):
        pygame.draw.circle(self.screen, (0,0,0), (x,y), 10, 10)
    
    def Draw_Black_Line(self,xBase,yBase,xTip,yTip,thickness):
        pygame.draw.line(self.screen, (0,0,0), (xBase, yBase), (xTip, yTip), thickness)
        
    def Draw_Progress_Bar(self, overall_ratio, previous_ratio, current_ratio):
        #if previous ratio good / total is lower then  good / total
        #pygame.draw.rect(screen, color, (x,y,width,height), thickness)
        #exterior border
        pygame.draw.rect(self.screen, (0,0,0), (10,430,280,30), 3)
        #interior colored box
        if ((current_ratio - previous_ratio) > 0.1):
            pygame.draw.rect(self.screen, (0,255,0), (12,432,(276*current_ratio),26), 0)
        elif (-0.1 < (current_ratio - previous_ratio) < 0.1):
            pygame.draw.rect(self.screen, (255,221,51), (12,432,(276*current_ratio),26), 0)
        else:
            pygame.draw.rect(self.screen, (255,0,0), (12,432,(276*current_ratio),26), 0)
        #pygame.draw.lines(screen, color, closed, pointlist, thickness)
        if (overall_ratio != previous_ratio):
            pygame.draw.lines(self.screen, (0,0,0), False, [(12+(276*overall_ratio), 420), (12+(276*overall_ratio), 470)], 3)
            self.startup_image = pygame.image.load(os.path.join("./group2.jpg"))
            self.startup_image = pygame.transform.scale(self.startup_image, (50, 50))
            rect = self.startup_image.get_rect()
            rect = rect.move((12+(276*overall_ratio)-25, 370))
            self.screen.blit(self.startup_image, rect)
        pygame.draw.lines(self.screen, (0,0,0), False, [(12+(276*previous_ratio), 420), (12+(276*previous_ratio), 470)], 3)
        self.startup_image = pygame.image.load(os.path.join("./individual_comp.png"))
        self.startup_image = pygame.transform.scale(self.startup_image, (50, 50))
        rect = self.startup_image.get_rect()
        rect = rect.move((12+(276*previous_ratio)-25, 370))
        self.screen.blit(self.startup_image, rect)
    
    def Draw_Hot_Cold_Bar(self, correct_predicted, incorrect_predicted):
        pygame.draw.rect(self.screen, (0,0,0), (10,330,230,30), 3)
        if (correct_predicted > incorrect_predicted):
            pygame.draw.rect(self.screen, (0,255,0), (12,332,int(226*(float(correct_predicted)/10)),26), 0)
            self.startup_image = pygame.image.load(os.path.join("./checkMark.png"))
            self.startup_image = pygame.transform.scale(self.startup_image, (50, 50))
            rect = self.startup_image.get_rect()
            rect = rect.move((12+226+25), (330 - 25))
            self.screen.blit(self.startup_image, rect)
        else:
            pygame.draw.rect(self.screen, (255,0,0), (12,332,int(226*(float(incorrect_predicted)/30)),26), 0)
            self.startup_image = pygame.image.load(os.path.join("./incorrect.png"))
            self.startup_image = pygame.transform.scale(self.startup_image, (50, 50))
            rect = self.startup_image.get_rect()
            rect = rect.move((12+226+25), (330 - 25))
            self.screen.blit(self.startup_image, rect)
        
    def Show_Image(self, imagePath):
        self.startup_image = pygame.image.load(os.path.join(imagePath))
        self.startup_image = pygame.transform.scale(self.startup_image, (300, 300))
        rect = self.startup_image.get_rect()
        rect = rect.move((300, 0))
        self.screen.blit(self.startup_image, rect)
        #self.screen.blit(self.startup_image, (0.02,0.02))
        
    def Show_Image_Lower(self, imagePath):
        self.startup_image = pygame.image.load(os.path.join(imagePath))
        self.startup_image = pygame.transform.scale(self.startup_image, (300, 300))
        rect = self.startup_image.get_rect()
        rect = rect.move((300, 300))
        self.screen.blit(self.startup_image, rect)
        
    def TicTakToeButton(self):
        button = pygame.Rect(100, 100, 50, 50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position
                # checks if mouse position is over the button
                if button.collidepoint(mouse_pos):
                    # prints current location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))
        pygame.draw.rect(self.screen, [255, 0, 0], button)
            