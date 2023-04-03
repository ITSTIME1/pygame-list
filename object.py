# 객체, (태선, h)
import pygame

class Object():
    def __init__(self):
        self.name = "홍태선"
        self.width = 720
        self.height = 720
        self.objImage = pygame.image.load("image/ship.png")
        self.objRect = self.objImage.get_rect()
    
    def position(self):
        self.objRect.centerx = self.width / 2
        self.objRect.centery = self.height / 2

