import pygame

class HeartObject():
    def __init__(self, imageNum):
        self.heartImageInit = pygame.image.load("image/heart" + str(imageNum) + ".png")
        self.heartImage = pygame.transform.scale(self.heartImageInit, (110, 80))
        # screen.blit(pygame.transform.scale(pic, (500, 500)), (0, 0))
        self.heartRect = self.heartImage.get_rect()
    
    # @TODO heart object 만들어야됨.
    def position(self, x, y):
        self.heartRect.x = x
        self.heartRect.y = y