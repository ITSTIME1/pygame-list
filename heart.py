import pygame

class HearyObject():
    def __init__(self, name):
        self.speed = 1.5
        self.heartImageInit = pygame.image.load("image/heart.png")
        self.heartImage = pygame.transform.scale(self.heartImageInit, (200, 150))
        # screen.blit(pygame.transform.scale(pic, (500, 500)), (0, 0))
        self.heartRect = self.heartImage.get_rect()
    
    # @TODO heart object 만들어야됨.
    def position(self, xpos, ypos): 
        self.heartRect.x = xpos
        self.heartRect.y = ypos