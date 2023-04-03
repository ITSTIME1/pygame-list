# 객체, (태선, h)
import pygame

class Object():
    def __init__(self):
        self.name = "홍태선"
        self.width = 720
        self.height = 720
        self.xpos = 720 / 2
        self.ypos = 720 / 2
        self.objImage = pygame.image.load("image/ship.png")
        self.objRect = self.objImage.get_rect()
    
    def position(self, xpos, ypos):
        self.objRect.x = xpos
        self.objRect.y = ypos