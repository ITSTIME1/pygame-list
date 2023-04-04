import pygame
import sys
# object py
import character
# 현재 Monterey 에서 지원을 하지 않아;;
# 왜 애플 실리콘 지원 안하는데;




# initialize pygame module
class InitPygame():
    # init pygame 
    def __init__(self):
        pygame.init()
        self.screen_size = (720, 720)
        self.clock = pygame.time.Clock().tick(30)
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("Haeun Game")
        self.initStart = True
        self.gameStart = True
        self.startBtn = False
        self.storeBtn = False
        self.exitBtn = False
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.xpos = self.width / 2 - 50
        self.ypos = self.height - 100
        self.name = "홍태선"
        pygame.mixer.music.load("audio/짱구는못말려.mp3")
        pygame.mixer.music.play()
        pygame.event.wait()
        self.initBackground = pygame.image.load("image/back.gif")
        self.screen.blit(self.initBackground, (0    , 0))
        # init object
        self.charObj = character.ChracterObject(self.name)
        
        # button rect
        self.rectWidth = 100
        self.rectHeight = 40
        
        
    def __setting__(self):
        self.initBackground
        self.screen.blit(self.initBackground, (0, 0))
        # initstate object
        # problem base 
        self.xpos = self.width / 2 - 50
        self.ypos = self.height / 2 + 200
        self.charObj.position(self.xpos, self.ypos)



        # self.startButton = False
        # self.storeButton = False
        # self.exitButton = False
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


        # btn rect
        startBtnRect = startBtnTitle.get_rect()
        storeBtnRect = storeBtnTitle.get_rect()
        exitBtnRect = exitBtnTitle.get_rect()

        # start width, height    
        startBtnWidth = startBtnTitle.get_width()
        # store width, height
        storeBtnWidth = storeBtnTitle.get_width()
        # exit width, height
        exitBtnWidth = exitBtnTitle.get_width()




        startBtnRect.x, startBtnRect.y = round(self.width/2-startBtnWidth/2), round(self.height/2 - 100 + 12)
        storeBtnRect.x, storeBtnRect.y = round(self.width/2-storeBtnWidth/2), round(self.height/2 - 30 + 12)
        exitBtnRect.x, exitBtnRect.y = round(self.width/2-exitBtnWidth/2), round(self.height/2 + 40 + 12)


        # mouse pos & rect
        # mouse recognition
        mouse = pygame.mouse.get_pos() 


        # start button
        if self.width/2 - 50 <= mouse[0] <= self.width/2 - 50 + 100 and self.height/2 - 100 <= mouse[1] <= self.height/2 - 100+40:
            pygame.draw.rect(self.screen,(254, 198, 223),[self.width/2 - 100/2, self.height/2 - 100, self.rectWidth, self.rectHeight], 0, 3)
            # 음 텍스트 안에 들어오면 어떨까
            self.width/2 - 100/2
            if self.startBtn == False:
                pygame.mixer.music.load("audio/mouseClick.wav")
                pygame.mixer.music.play()
                pygame.event.wait() 
                self.startBtn = True 

            if pygame.mouse.get_pressed(3)[0] == True:
                self.gameStart = False
                self.startBtn = False
            else:
                print("start area")


        # score 상태저장소
        if self.width/2 - 50 <= mouse[0] <= self.width/2 - 50 + 100 and self.height/2 - 30 <= mouse[1] <= self.height/2 - 30+40: 
            pygame.draw.rect(self.screen,(163, 159, 225),[self.width/2 - 100/2, self.height/2 - 30, self.rectWidth, self.rectHeight], 0, 3)
            
            if self.storeBtn == False:
                pygame.mixer.music.load("audio/mouseClick.wav")
                pygame.mixer.music.play()
                pygame.event.wait()
                self.storeBtn = True

            # print("store area")
            # if pygame.mouse.get_pressed(3)[0] == True:
            #     # goto store database
            # else:
            #     pass

        # 게임종료
        if self.width/2 - 50 <= mouse[0] <= self.width/2 - 50 + 100 and self.height/2 + 40 <= mouse[1] <= self.height/2 + 40+40:        
            pygame.draw.rect(self.screen,(34, 118, 148),[self.width/2 - 100/2, self.height/2 + 40, self.rectWidth, self.rectHeight], 0, 3)         
            
            if self.exitBtn == False:
                pygame.mixer.music.load("audio/mouseClick.wav")
                pygame.mixer.music.play()
                pygame.event.wait()
                self.exitBtn = True

            if pygame.mouse.get_pressed(3)[0] == True:
                # pygame.display.quit()
                # 게임 자체 종료
                # 이걸 그대로 써도 되나
                # 만약 게임이 실행중이었고 store 저장할건지를 물어봐줘야될거 같은데
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
            

            if self.initStart == True and self.gameStart == False:
                self.__startGame__()
            else:
                self.__setting__()
            

            # what ?
            pygame.display.flip()
            # pygame.display.update()




    def __startGame__(self):
        startBackground = pygame.image.load("image/gameStart.jpg")
        self.screen.blit(startBackground, (0, 0))
        
        
        # when key pressed
        keyPressed = pygame.key.get_pressed()
        
        
        # 오른쪽으로 이동
        if keyPressed[pygame.K_RIGHT] == True:
            self.xpos += 30 * self.charObj.speed
            # 만약 범위를 넘어가게 된다면
            if self.xpos > 560:
                print("못가요")
                self.xpos = 560
            else:
                self.charObj.position(self.xpos, self.ypos)
        # 왼쪽으로 이동
        elif keyPressed[pygame.K_LEFT] == True:
            self.xpos -= 30 * self.charObj.speed
            if self.xpos < 0:
                print("못가요")
                self.xpos = 0
            else:
                self.charObj.position(self.xpos, self.ypos)

        elif keyPressed[pygame.K_ESCAPE] == True:
            # 스코어 정보를 저장해주어야 하고 db에 저장을 하는게 좋을거 같긴한데
            # 음..
            # 이건 좀 생각해보자
            self.gameStart = True
            self.startBtn = False
            self.storeBtn = False
            self.exitBtn = False

        self.screen.blit(self.charObj.charImage, self.charObj.charRect)


        # pressed가 중요
        # 어떤 키를 눌렀을때 x, y를 업데이트 해줄건지
        # 음 근데 false를



        

if __name__ == '__main__':
    game = InitPygame()
    # 게임 분기처리.
    game.__initGame__()
    