import pygame
import constants


class PYGAME_WINDOW:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((constants.pygameWindowWidth,constants.pygameWindowDepth))
        
    def Prepare(self):
        pygame.event.get()
        self.screen.fill((255,255,255))
        
    def Reveal(self):
        pygame.display.update()