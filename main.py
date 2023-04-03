import pygame
import sys
# object py
import object

# initialize pygame module
class InitPygame():
    # init pygame 
    def __init__(self):
        pygame.init()
        self.screen_size = (720, 720)
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("Menu")
        self.initStart = True
        self.gameStart = True
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        pygame.mixer.music.load("audio/짱구는못말려.mp3")
        pygame.mixer.music.play()
        pygame.event.wait()
        self.background = pygame.image.load("image/back.gif")
        self.screen.blit(self.background, (0, 0))
        
        # button rect
        self.rectWidth = 100
        self.rectHeight = 40
        
        
    def __setting__(self):
        self.startButton = False
        self.storeButton = False
        self.exitButton = False
        self.fontName = "font/Maplestory OTF Bold.otf"
        self.font = pygame.font.Font(self.fontName, 30)
        self.mainFont = pygame.font.Font(self.fontName, 15)
        self.textTitle = self.font.render("하늘에서 하은이가?", True, (255, 255, 255))
        self.textRect = self.textTitle.get_rect()
        self.textRect.centerx, self.textRect.y = round(720 / 2), round(720 / 2 - 240)
        self.screen.blit(self.textTitle, self.textRect)
        pygame.draw.rect(self.screen,(0, 0, 0),[self.width/2 - 100/2, self.height/2 - 100, self.rectWidth, self.rectHeight], 0, 3)
        pygame.draw.rect(self.screen,(0, 0, 0),[self.width/2 - 100/2, self.height/2 - 30, self.rectWidth, self.rectHeight], 0, 3)
        pygame.draw.rect(self.screen,(0, 0, 0),[self.width/2 - 100/2, self.height/2 + 40, self.rectWidth, self.rectHeight], 0, 3) 
        startBtnTitle = self.mainFont.render("시작", True, (255, 255, 255))
        storeBtnTitle = self.mainFont.render("저장", True, (255, 255, 255))
        exitBtnTitle = self.mainFont.render("종료", True, (255, 255, 255))


        startBtnRect = startBtnTitle.get_rect()
        storeBtnRect = storeBtnTitle.get_rect()
        exitBtnRect = exitBtnTitle.get_rect()

        # start width, height    
        startBtnWidth, startBtnHeight = startBtnTitle.get_width(), startBtnTitle.get_height()
        # store width, height
        storeBtnWidth, storeBtnHeight = storeBtnTitle.get_width(), storeBtnTitle.get_height()
        # exit width, height
        exitBtnWidth, exitBtnHeight = exitBtnTitle.get_width(), exitBtnTitle.get_height()




        startBtnRect.x, startBtnRect.y = round(self.width/2-startBtnWidth/2), round(self.height/2 - 100 + 12)
        storeBtnRect.x, storeBtnRect.y = round(self.width/2-storeBtnWidth/2), round(self.height/2 - 30 + 12)
        exitBtnRect.x, exitBtnRect.y = round(self.width/2-exitBtnWidth/2), round(self.height/2 + 40 + 12)





        # mouse pos & rect
        # mouse recognition
        mouse = pygame.mouse.get_pos() 


        # start button
        if self.width/2 - 100/2 <= mouse[0] <= self.width/2 - 100/2+100 and self.height/2 - 100 <= mouse[1] <= self.height/2 - 100+40:
            pygame.draw.rect(self.screen,(254, 198, 223),[self.width/2 - 100/2, self.height/2 - 100, self.rectWidth, self.rectHeight], 0, 3)

            # 시작 버튼을 클릭했다면 게임 시작
            if self.startButton == False:
                pygame.mixer.music.load("audio/mouseClick.wav")
                pygame.mixer.music.play()
                pygame.event.wait()
                self.startButton = True

            if pygame.mouse.get_pressed(3)[0] == True:
                self.gameStart = False
            else:
                print("start area")


        # score 상태저장소
        if self.width/2 - 100/2 <= mouse[0] <= self.width/2 - 100/2+100 and self.height/2 - 30 <= mouse[1] <= self.height/2 - 30+40: 
            pygame.draw.rect(self.screen,(163, 159, 225),[self.width/2 - 100/2, self.height/2 - 30, self.rectWidth, self.rectHeight], 0, 3)


            if self.storeButton == False:
                pygame.mixer.music.load("audio/mouseClick.wav")
                pygame.mixer.music.play()
                pygame.event.wait()
                self.storeButton = False
            
            # print("store area")
            # if pygame.mouse.get_pressed(3)[0] == True:
            #     # goto store database
            # else:
            #     pass

        # 게임종료
        if self.width/2 - 100/2 <= mouse[0] <= self.width/2 - 100/2+100 and self.height/2 + 40 <= mouse[1] <= self.height/2 + 40+40:        
            pygame.draw.rect(self.screen,(34, 118, 148),[self.width/2 - 100/2, self.height/2 + 40, self.rectWidth, self.rectHeight], 0, 3)         


            if self.exitButton == False:
                pygame.mixer.music.load("audio/mouseClick.wav")
                pygame.mixer.music.play()
                pygame.event.wait()
                self.exitButton = True
        

            if pygame.mouse.get_pressed(3)[0] == True:
                # pygame.display.quit()
                # 게임 자체 종료
                sys.exit()
                print("exit area")



        self.screen.blit(startBtnTitle, startBtnRect)
        self.screen.blit(storeBtnTitle, storeBtnRect)
        self.screen.blit(exitBtnTitle, exitBtnRect)

        # footer
        footerTitle = self.mainFont.render("Designed by itstime", True, (255, 255, 255))
        footerRect = footerTitle.get_rect()
        footerRect.centerx, footerRect.y = round(self.width / 2), round(self.height-50)
        self.screen.blit(footerTitle, footerRect)


    def __initGame__(self):
        while self.initStart != False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.initStart = False
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.width/2 <= pygame.mouse.get_pressed(3)[0] <= self.width/2+140 and self.height/2 <= pygame.mouse.get_pressed(3)[1] <= self.height/2+40: 
                    if pygame.mouse.get_pressed(3)[0] == True:
                        # uninitialize pygame module
                        pygame.quit()
            # 게임은 진행중인데 gameStart 는 True다

            if self.initStart == True and self.gameStart == False:
                self.__startGame__()
            else:
                self.__setting__()

            pygame.display.update()

    def __startGame__(self):
        # 객체를 생성해주고
        obj = object.Object()
        self.screen.fill((255, 255, 255))
        self.background = pygame.image.load("image/gameStart.jpg")
        self.screen.blit(self.background, (0, 0))

        self.screen.blit(obj.objImage, obj.objRect)


        # when key pressed
        keyPressed = pygame.key.get_pressed()  
        


        if keyPressed[pygame.K_RIGHT] == True:
            print("오른쪽")
        
        elif keyPressed[pygame.K_LEFT] == True:
            print("왼쪽")

        elif keyPressed[pygame.K_ESCAPE] == True:
            self.gameStart = True
            



        # pressed가 중요
        # 어떤 키를 눌렀을때 x, y를 업데이트 해줄건지
        # 음 근데 false를

    

        

if __name__ == '__main__':
    game = InitPygame()
    # 게임 분기처리.
    game.__initGame__()
    