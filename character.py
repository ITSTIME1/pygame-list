# 객체, (태선, h)
import pygame

class ChracterObject():
    def __init__(self, name):
        self.name = name
        # 잔소리 말고 하트를 먹으면 speed가 일정 비율로 올라가게 해도 될거 같은데
        # 아니면 하트를 먹을때 마다 올라가니까 그렇게 말고
        # 특정 개수 만큼 채우면 잠깐 동안 피버타임이라고 그래서 speed 값을 일정 시간동안만 유지하는거지
        # 그렇게 해도 될듯?
        self.speed = 1.5
        self.width = 720
        self.height = 720
        self.charImageInit = pygame.image.load("image/png/Dead (1).png")
        self.charImage = pygame.transform.scale(self.charImageInit, (200, 150))
        # screen.blit(pygame.transform.scale(pic, (500, 500)), (0, 0))
        self.charRect = self.charImage.get_rect()
    
    def position(self, xpos, ypos):
        self.charRect.x = xpos
        self.charRect.y = ypos

