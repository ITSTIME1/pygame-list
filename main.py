import random
import pygame
import sys
# object py
import character
import heart
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
        self.screen.blit(self.initBackground, (0, 0))
        # char object init
        self.charObj = character.ChracterObject(self.name)
        # heart object init
        self.heartObj_1 = heart.HeartObject(1)
        self.heartObj_2 = heart.HeartObject(2)
        self.heartObj_3 = heart.HeartObject(3)
        self.heartObj_4 = heart.HeartObject(4)

        # 여러개면됨 지금은 테스트로써 하나만 있다고 가정하고
        self.heartObjList = [self.heartObj_1, 
                             self.heartObj_2, 
                             self.heartObj_3, 
                             self.heartObj_4]
        
        self.h = random.choice(self.heartObjList)
        self.hX = random.randint(0, self.width - self.h.heartRect.width)
        self.hY = -10
        self.hSpeed = 3
        
        # button rect
        self.rectWidth = 100
        self.rectHeight = 40


        # speed improve
        self.count = 0
        self.score = 0
        
        
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

    def heartDraw(self):
        self.hY += self.hSpeed
        if self.hY > self.height:
            self.count += 1
            # 땅에 떨어진 물체가 3개가 된다면
            # hSpeed 떨어지는 스피드를 2배씩 증가
            if self.count == 2:
                self.count = 0
                self.hSpeed *=2
            self.h = random.choice(self.heartObjList)
            self.hX, self.hY = random.randint(0, self.width - self.h.heartRect.width), -10 
        
        # 음 물체의 위치랑
        # 플레이어의 현재 y위치 와 물체의 y위치가 플에이어의 위치보다 크거나 같다면 충돌

        # 0% 하트
        # @TODO 세세한거 더해야됨
        if self.h == self.heartObj_4:
            # 생각해보니까 좌표로만 따지고 있네;;
            # 충돌을 따로 생각해야되겟ㄷ 
            if self.charObj.charRect.collidepoint(self.hX, self.hY) == True:
                print("게임종료")  
                self.gameStart = True
                # 초기화
                # 게임 자체 초기화
                self.__init__()
        else:
            if self.charObj.charRect.collidepoint(self.hX, self.hY) == True:
                self.score += 1
                self.h = random.choice(self.heartObjList)
                self.hX, self.hY = random.randint(0, self.width - self.h.heartRect.width), -10

        
        return self.screen.blit(self.h.heartImage, (self.hX, self.hY))



    

    def __startGame__(self):
        startBackground = pygame.image.load("image/gameStart.jpg")
        self.screen.blit(startBackground, (0, 0))

        self.fontName = "font/Maplestory OTF Bold.otf"  
        self.font = pygame.font.Font(self.fontName, 30)
        self.mainFont = pygame.font.Font(self.fontName, 15)
        # Score text
        self.scoreTitle = self.font.render("Score : " + str(self.score), True, (255, 255, 255))
        self.scoreRect = self.scoreTitle.get_rect()
        # 상단
        self.scoreRect.x, self.scoreRect.y = 10, 10
        self.screen.blit(self.scoreTitle, self.scoreRect)

        # 일정 점수이상 도달하게 된다면
        # 맵의 이미지가 바뀌는 것도 구현할 수 있겠네
        # when key pressed
        # 그걸 해도 되겠따 게임 스타트 버튼을 눌렀을때
        # 이름을 적게 하고
        # 만약 그 이름이 홍태선이라고 한다면
        # 홍태선 너 못하면 죽을줄 알아...
        # 하는 텍스트가 서서히 나타나고 다 나타났으면 서서히 사라지면서
        # 맵이 서서히 보이고
        # 다 보였으면
        # 3, 2, 1 GameStart 라는 텍스트를 출력하고
        # 게임이 시작되는거지 바로 시작되는게 아니라
        # 그렇게 되면서 score가 그려지게 되고 위에
        # 점수를 얻을때마다 스코어의 점수를 올려주면 바로 갱신이 될 수 있도록 해주고
        # 하니 얼굴이 좌우로 움직이면서 즉 좌표값을 계속 업데이트하면서
        # 하트나 혹은 잔소리를 내뿜는거지
        # 하트먹으면 score += 1
        # 0퍼센트 하트 먹으면 score -= 1
        keyPressed = pygame.key.get_pressed()
        
        # heartObject create
        self.heartDraw()

        # wordDraw()
        
        
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
    