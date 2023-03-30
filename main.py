import pygame
import random
from math import sin
from math import cos
from math import radians

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
    x = random.randrange(-20, 400)
    y = random.randrange(0, 400)

    # 값이 바뀌어야 하니까 튜플x
    snowFall.append([x, y])


clock = pygame.time.Clock()



def init(canvas):
    # font
    font_name = "font/Maplestory OTF Bold.otf"
    canvas.fill(black_color)
    font = pygame.font.Font(font_name, 30)
    text_title = font.render("text", True, black_color)

    text_rect = text_title.get_rect()

    text_rect.centerx, text_rect.y = round(400 / 2), round(400 / 2)

    canvas.blit(text_title, text_rect)



# canvas 자체가 좌표계가 최상단 왼쪽부터 시작함.
# 최상단 왼쪽이 (0, 0) 오른쪽 갈수록 양수로 증가
# canvas 내에서는 전부 양수값이네
# 그럼 (0,0 ) 위쪽으로 가면 y값이 -가 되고, (0, 0) 을 기준으로 왼쪽이 되니까

def snowLoop(snowBall, canvas):
    for i in range(len(snowBall)):
        radius = random.randint(0, 4)
        # color = [r, g, b]
        pygame.draw.circle(canvas, 
                           [random.randint(0, 255), 
                            random.randint(0, 255), 
                            random.randint(0, 255)], 
                            snowBall[i], radius)
        # 스노우볼 업데이트
        snowBall[i][1] += 1
        print(snowBall)

        # snowFall이 화면 밖을 나갔을 경우
        # x와 y의 좌표값을 화면이 밖에 나갔을 경우로 한정지어주는데
        if snowBall[i][1] > 400:   
            # y값을 -로 설정한이유
            # (x, y) 
            y = random.randrange(-10, 400)
            snowBall[i][1] = y

            x = random.randrange(0, 400)
            snowBall[i][0] = x
    

# Draws a rose with n petals and of radius size about `size`
# def drawRhodoneaCurve(n, d, size):
#     points =[]
#     for i in range(0, 361):
#         # The equation of a rhodonea curve
#         k = i * d
#         r = size * sin(radians(n * k))
 
#         # Converting to cartesian co-ordinates
#         x = r * cos(radians(k))
#         y = r * sin(radians(k))


#         # rgb color select
#         r = random.randint(0, 255)
#         g = random.randint(0, 255)
#         b = random.randint(0, 255)
 
#         list.append(points, (400 / 2 + x, 400 / 2 + y))
 
#     pygame.draw.lines(canvas, (0, 0, 0), False, points, 5)
 
# def drawPattern():
#     # Try changing these values to what you want
#     drawRhodoneaCurve(6, 79, 400)


pygame.display.flip()
while not exit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
    init(canvas)
    snowLoop(snowFall, canvas)
    # drawPattern()

    # pygame.display.update()
    pygame.display.flip()
    # clock.tick(20)
    
    
pygame.quit()