import pygame
import constants
import os


class PYGAME_WINDOW:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((constants.pygameWindowWidth,constants.pygameWindowDepth))
        pygame.font.init()
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)
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
        self.screen.blit(textsurface,(0,0))
        
    def Draw_Black_Circle(self,x,y):
        pygame.draw.circle(self.screen, (0,0,0), (x,y), 10, 10)
    
    def Draw_Black_Line(self,xBase,yBase,xTip,yTip,thickness):
        pygame.draw.line(self.screen, (0,0,0), (xBase, yBase), (xTip, yTip), thickness)
        
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
        