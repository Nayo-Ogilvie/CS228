import pygame
import constants


class PYGAME_WINDOW:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((constants.pygameWindowWidth,constants.pygameWindowDepth))
        pygame.font.init()
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)
        
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