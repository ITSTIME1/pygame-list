import pygame


# initialize pygame module
pygame.init()


# screen_size 720 * 720
screen_size = (720, 720)

# setting screen size
screen = pygame.display.set_mode(screen_size)

# width, height
width, height = screen.get_width(), screen.get_height()

# width = 720, height = 720

stWidth = 100
stHeight = 40



# print(width, height)
# initialize
def init():
    # screen fill
    screen.fill((252, 245, 239)) 

    # title
    pygame.display.set_caption("Menu")


# start screen
def start():
    # top 
    fontName = "font/Maplestory OTF Bold.otf"
    font = pygame.font.Font(fontName, 30)
    mainFont = pygame.font.Font(fontName, 15)
    textTitle = font.render("하늘에서 하은이가?", True, (0, 0, 0), (255, 255, 255))
    textRect = textTitle.get_rect()
    textRect.centerx, textRect.y = round(720 / 2), round(720 / 2 - 240)
    screen.blit(textTitle, textRect)

    pygame.draw.rect(screen,(0, 0, 0),[width/2 - 100/2, height/2 - 100, stWidth, stHeight], 0, 3)
    pygame.draw.rect(screen,(0, 0, 0),[width/2 - 100/2, height/2 - 30, stWidth, stHeight], 0, 3)
    pygame.draw.rect(screen,(0, 0, 0),[width/2 - 100/2, height/2 + 40, stWidth, stHeight], 0, 3) 
    
    startBtnTitle = mainFont.render("시작", True, (255, 255, 255))
    storeBtnTitle = mainFont.render("저장", True, (255, 255, 255))
    exitBtnTitle = mainFont.render("종료", True, (255, 255, 255))


    startBtnRect = startBtnTitle.get_rect()
    storeBtnRect = storeBtnTitle.get_rect()
    exitBtnRect = exitBtnTitle.get_rect()

    # start width, height    
    startBtnWidth, startBtnHeight = startBtnTitle.get_width(), startBtnTitle.get_height()
    # store width, height
    storeBtnWidth, storeBtnHeight = storeBtnTitle.get_width(), storeBtnTitle.get_height()
    # exit width, height
    exitBtnWidth, exitBtnHeight = exitBtnTitle.get_width(), exitBtnTitle.get_height()
    



    startBtnRect.x, startBtnRect.y = round(width/2-startBtnWidth/2), round(height/2 - 100 + 12)
    storeBtnRect.x, storeBtnRect.y = round(width/2-storeBtnWidth/2), round(height/2 - 30 + 12)
    exitBtnRect.x, exitBtnRect.y = round(width/2-exitBtnWidth/2), round(height/2 + 40 + 12)





    # mouse pos & rect
    # mouse recognition
    mouse = pygame.mouse.get_pos() 
    if width/2 - 100/2 <= mouse[0] <= width/2 - 100/2+100 and height/2 - 100 <= mouse[1] <= height/2 - 100+40:
        pygame.draw.rect(screen,(254, 198, 223),[width/2 - 100/2, height/2 - 100, stWidth, stHeight], 0, 3)
        # print("start area")

    if width/2 - 100/2 <= mouse[0] <= width/2 - 100/2+100 and height/2 - 30 <= mouse[1] <= height/2 - 30+40: 
        pygame.draw.rect(screen,(163, 159, 225),[width/2 - 100/2, height/2 - 30, stWidth, stHeight], 0, 3)
        # print("store area")


    if width/2 - 100/2 <= mouse[0] <= width/2 - 100/2+100 and height/2 + 40 <= mouse[1] <= height/2 + 40+40:        
        pygame.draw.rect(screen,(34, 118, 148),[width/2 - 100/2, height/2 + 40, stWidth, stHeight], 0, 3)         
        # print("exit area")




    screen.blit(startBtnTitle, startBtnRect)
    screen.blit(storeBtnTitle, storeBtnRect)
    screen.blit(exitBtnTitle, exitBtnRect)


    # footer
    footerTitle = mainFont.render("Designed by itstime", True, (0, 0, 0))
    footerRect = footerTitle.get_rect()
    footerRect.centerx, footerRect.y = round(width / 2), round(height-50)
    screen.blit(footerTitle, footerRect)


# font setting
def font():
    font_name = font_name = "font/Maplestory OTF Bold.otf"
    font = pygame.font.Font(font_name, 10)
    


gameStart = True
while gameStart != False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gaemStart = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
        
            if width/2 <= pygame.mouse.get_pressed(3)[0] <= width/2+140 and height/2 <= pygame.mouse.get_pressed(3)[1] <= height/2+40: 
                if pygame.mouse.get_pressed(3)[0] == True:
                    # uninitialize pygame module
                    pygame.quit()
    
    # init screen & title 
    init()
    # start
    start()
    # font setting
    font()

    mouse = pygame.mouse.get_pos()  

    pygame.display.update()



# 시작화면 구성
# 메뉴 화면 구성
# 틱택톡 게임 시작




    