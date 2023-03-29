import pygame
import random


pygame.init()

# print(pygame.font.get_fonts)

white_color = (255, 255, 255)
black_color = (0, 0, 0)
rect_color = (255,0,0)
window_size = (400, 400)
snowFall_max = 50
  
# CREATING CANVAS
canvas = pygame.display.set_mode(window_size)
  
# TITLE OF CANVAS
pygame.display.set_caption("SnowBall")
  
# image = pygame.image.load("Screenshot.png")
exit = False
  
snowFall = []
for i in range(snowFall_max):
    # start, end is 400
    x = random.randrange(0, 400)
    y = random.randrange(0, 400)
    snowFall.append([x, y])


clock = pygame.time.Clock()



def init(canvas):
    font_name = "font/Maplestory OTF Bold.otf"
    canvas.fill(black_color)
    font = pygame.font.Font(font_name, 30)
    text_title = font.render("하은이는 뭐할까?", True, white_color)

    text_rect = text_title.get_rect()

    text_rect.centerx = round(400 / 2)

    text_rect.y = 50

    canvas.blit(text_title, text_rect)


def snowLoop(snowList, canvas):
    for i in range(len(snowList)):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        color = [r, g, b]
        radius = random.randint(0, 5)
        pygame.draw.circle(canvas, color, snowList[i], radius)
        snowList[i][1] += 1

        # snowFall이 화면 밖을 나갔을 경우
        if snowList[i][1] > 400:    
            y = random.randrange(-100, 10)
            snowList[i][1] = y

            x = random.randrange(0, 400)
            snowList[i][0] = x

while not exit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
    init(canvas)
    snowLoop(snowFall, canvas)

    pygame.display.flip()
    clock.tick(20)
    
    
pygame.quit()