import sys
import pygame, sys,time,random
from pygame.locals import *

pygame.init()  #初始化pygame
screen = pygame.display.set_mode((1280, 720)) #設定畫面大小(1280, 720)
pygame.display.set_caption("自主學習遊戲") #設定畫面標題

road_y = [72+27,72+27+108+135,72+27+108+135+108+135]

#資源
hunting_level = 0 #hunter資源等級
logging_level = 0 #logger資源等級
meat_resource = 501 #meat資源
wood_resource = 501 #wood資源

#圖片匯入
if "image_load" == "image_load":
    #道路 匯入
    Road_image = pygame.image.load("road.png")
    Road_image_rect = Road_image.get_rect()

    #森林匯入
    Forest_image = pygame.image.load("forest.png")
    Forest_image_rect = Forest_image.get_rect()

    #房子匯入
    House_image = pygame.image.load("house.png")
    House_image_rect = House_image.get_rect()

    #空豬圈匯入
    Pigsty_image = pygame.image.load("pigsty.png")
    Pigsty_image_rect = Pigsty_image.get_rect()

    #資源圖示匯入
    meat_resource_image = pygame.image.load("meat_resource_image.png")#肉
    wood_resource_image = pygame.image.load("wood_resource_image.png")#木頭

    #經驗值、血量圖示匯入
    ex_value_image = [pygame.image.load("ex0.png"),
                      pygame.image.load("ex1.png"),
                      pygame.image.load("ex2.png"),
                      pygame.image.load("ex3.png"),
                      pygame.image.load("ex4.png"),
                      pygame.image.load("ex5.png"),
                      pygame.image.load("ex6.png"),
                      pygame.image.load("ex7.png"),
                      pygame.image.load("ex8.png"),
                      pygame.image.load("ex9.png"),
                      pygame.image.load("ex10.png"),
                      pygame.image.load("ex11.png"),
                      pygame.image.load("ex12.png"),
                      pygame.image.load("ex13.png"),
                      pygame.image.load("ex14.png"),
                      pygame.image.load("ex15.png"),
                      pygame.image.load("ex16.png"),
                      pygame.image.load("ex17.png"),
                      pygame.image.load("ex18.png"),
                      pygame.image.load("ex19.png"),
                      pygame.image.load("ex20.png"),
                      pygame.image.load("ex21.png"),]
    hp_value_image = [pygame.image.load("hp1.png"),
                      pygame.image.load("hp2.png"),
                      pygame.image.load("hp3.png"),
                      pygame.image.load("hp4.png"),
                      pygame.image.load("hp5.png"),
                      pygame.image.load("hp6.png"),
                      pygame.image.load("hp7.png"),
                      pygame.image.load("hp8.png"),
                      pygame.image.load("hp9.png"),
                      pygame.image.load("hp10.png"),]
    
    #選單按鈕匯入
    #knight
    KnightButton_image = pygame.image.load("knight_button.png")
    KnightButton_image_rect = KnightButton_image.get_rect()
    KnightButton_image_rect.topleft = (0,170)

    #獵人
    HunterButton_image = pygame.image.load("hunter_button.png")
    HunterButton_image_rect = HunterButton_image.get_rect()
    HunterButton_image_rect.topleft = (0,72)
    
    #伐木工
    LoggerButton_image = pygame.image.load("logger_button.png")
    LoggerButton_image_rect = LoggerButton_image.get_rect()
    LoggerButton_image_rect.topleft = (81,72)

#Player類別
class Player:
    def __init__(self, x, y, action):
        # player 的位置
        self.x = x
        self.y = y
        
        # 加載stand和attack和run的圖片
        self.stand_images = [pygame.image.load("player_stand.png")]

        self.attack_images = [pygame.image.load("player_attack1.png"), 
                              pygame.image.load("player_attack2.png")]

        self.run_images = [pygame.image.load("player_run1.png"),
                           pygame.image.load("player_run2.png"),
                           pygame.image.load("player_run3.png"),
                           pygame.image.load("player_run4.png"),
                           pygame.image.load("player_run5.png")]
        
        # 設定初始圖片與動畫狀態
        self.current_image = 0
        self.animation_speed = 0.6  # 控制動畫速度 數字越大更新越快
        self.action = action  # 預設行為是stand
        self.image = self.run_images[self.current_image]

    def update(self):
        # 更新 player 的動畫
        self.current_image += self.animation_speed

        if self.action == "stand":
            if self.current_image >= len(self.stand_images):
                self.current_image = 0
            self.image = self.stand_images[int(self.current_image)]
        
        if self.action == "run":
            if self.current_image >= len(self.run_images):
                self.current_image = 0
            self.image = self.run_images[int(self.current_image)]
        
        elif self.action == "attack":
            if self.current_image >= len(self.attack_images):
                self.current_image = 0
            self.image = self.attack_images[int(self.current_image)]

    def draw(self, surface):
        # 將 player 畫在指定的位置上
        surface.blit(self.image, (self.x, self.y))

#Slime類別
class Slime:
    def __init__(self, x, y, action):
        # Slime 的位置
        self.x = x
        self.y = y
        
        # 加載攻擊和奔跑的圖片
        self.attack_images = [pygame.image.load("slime_attack1.png"), 
                              pygame.image.load("slime_attack2.png")]
        self.run_images = [pygame.image.load("slime_run1.png"),
                           pygame.image.load("slime_run2.png"),
                           pygame.image.load("slime_run3.png"),
                           pygame.image.load("slime_run4.png"),
                           pygame.image.load("slime_run5.png")]
        
        # 設定初始圖片與動畫狀態
        self.current_image = 0
        self.animation_speed = 0.1  # 控制動畫速度 數字越大更新越快
        self.action = action  # 預設行為是跑動
        self.image = self.run_images[self.current_image]

    def update(self):
        # 更新 Slime 的動畫
        self.current_image += self.animation_speed
        if self.action == "run":
            if self.current_image >= len(self.run_images):
                self.current_image = 0
            self.image = self.run_images[int(self.current_image)]
        elif self.action == "attack":
            if self.current_image >= len(self.attack_images):
                self.current_image = 0
            self.image = self.attack_images[int(self.current_image)]

    def draw(self, surface):
        # 將 Slime 畫在指定的位置上
        surface.blit(self.image, (self.x, self.y))

#Dragon類別
class Dragon:
    def __init__(self, x, y, action):
        # Dragon 的位置
        self.x = x
        self.y = y
        self.last_attack_time = None
        # 加載攻擊和奔跑的圖片
        self.attack_images = [pygame.image.load("dragon_attack1.png"), 
                              pygame.image.load("dragon_attack2.png"),
                              pygame.image.load("dragon_attack3.png")]
        self.run_images = [pygame.image.load("dragon_run1.png"),
                           pygame.image.load("dragon_run2.png"),
                           pygame.image.load("dragon_run3.png"),
                           pygame.image.load("dragon_run4.png"),]
        
        # 設定初始圖片與動畫狀態
        self.current_image = 0
        self.animation_speed = 0.15  # 控制動畫速度 數字越大更新越快
        self.action = action  # 預設行為是跑動
        self.image = self.run_images[self.current_image]

    def update(self):
        # 更新 Dragon 的動畫
        self.current_image += self.animation_speed
        if self.action == "run":
            if self.current_image >= len(self.run_images):
                self.current_image = 0
            self.image = self.run_images[int(self.current_image)]
        elif self.action == "attack":
            if self.current_image >= len(self.attack_images):
                self.current_image = 0
            self.image = self.attack_images[int(self.current_image)]

    def draw(self, surface):
        # 將 Slime 畫在指定的位置上
        surface.blit(self.image, (self.x, self.y))

#Knight類別
class Knight:
    def __init__(self, x, y, action):
        self.x=x
        self.y=y
        self.hp_value=10
        self.attack_time=None
        # 加載攻擊和奔跑的圖片
        self.attack_images = [pygame.image.load("knight_attack1.png"), 
                              pygame.image.load("knight_attack2.png"),
                              pygame.image.load("knight_attack3.png"),
                              pygame.image.load("knight_attack4.png"),]
        self.run_images = [pygame.image.load("knight_run1.png"),
                           pygame.image.load("knight_run2.png"),
                           pygame.image.load("knight_run3.png")]
        
        # 設定初始圖片與動畫狀態
        self.current_image = 0
        self.animation_speed = 0.15  # 控制動畫速度 數字越大更新越快
        self.action = action  # 預設行為是跑動
        self.image = self.run_images[self.current_image]

    def update(self):
        # 更新 Knight 的動畫
        self.current_image += self.animation_speed
        if self.action == "run":
            if self.current_image >= len(self.run_images):
                self.current_image = 0
            self.image = self.run_images[int(self.current_image)]
        elif self.action == "attack":
            if self.current_image >= len(self.attack_images):
                self.current_image = 0
            self.image = self.attack_images[int(self.current_image)]

    def draw(self, surface):
        # 將 Knight 畫在指定的位置上
        surface.blit(self.image, (self.x, self.y))

#Tower類別
class Tower:
    def __init__(self, x, y, action):
        # Tower 的位置
        self.x = x
        self.y = y
        self.last_attack_time = None

        # 加載常設和攻擊的圖片
        self.standing_images = [pygame.image.load("tower_standing1.png"),
                                pygame.image.load("tower_standing2.png"),]
        self.attack_images = [pygame.image.load("tower_attack1.png"),
                              pygame.image.load("tower_attack2.png"),
                              pygame.image.load("tower_attack3.png"),
                              pygame.image.load("tower_attack2.png"),]
        
        # 設定初始圖片與動畫狀態
        self.current_image = 0
        self.action = action  # 預設行為是跑動
        self.image = self.standing_images[self.current_image]

        if self.action == "attack":
            self.animation_speed = 0.57  # 控制動畫速度 數字越大更新越快
        elif self.action == "standing":
            self.animation_speed = 0.07  # 控制動畫速度 數字越大更新越快


    def update(self):
        # 更新 Tower 的動畫
        self.current_image += self.animation_speed
        if self.action == "standing":
            if self.current_image >= len(self.standing_images):
                self.current_image = 0
            self.image = self.standing_images[int(self.current_image)]
        elif self.action == "attack":
            if self.current_image >= len(self.attack_images):
                self.current_image = 0
            self.image = self.attack_images[int(self.current_image)]

    def draw(self, surface):
        # 將 Tower 畫在指定的位置上
        surface.blit(self.image, (self.x, self.y-15))

# 創建文字圖像
font = pygame.font.Font("C:\Windows\Fonts\Bahnschrift.ttf", 64)#設定字型和大小（第二個參數是字型大小） None 代表使用 Pygame 預設字型
#(文字內容,抗鋸齒效果,顏色)
game_over_font = pygame.font.Font("C:\Windows\Fonts\Bahnschrift.ttf", 200)#設定字型和大小
game_over_text = game_over_font.render(f"game over",True,(255,255,255))

#等待遊戲開始
def WaitingForGameStart():
    waiting=True
    start_button_image=pygame.image.load("GameStart.png")
    start_button_image_rect=start_button_image.get_rect()
    start_button_image_rect.center=(1280/2,720/2)
    screen.blit(start_button_image,start_button_image_rect)
    pygame.display.update()
    while waiting:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if start_button_image_rect.collidepoint(mouse_pos):
                    waiting = False

#pigsty1 hunting動畫顯示、事件處理
pigsty1_current = 0
def pigsty1_hunting(hunting_speed):

    #meat資源更新
    global meat_resource, hunting_level
    meat_resource = hunting_level+meat_resource
    meat_resource_text = font.render(f"{meat_resource}", True, (255,255,255))#肉資源文字物件
    screen.blit(meat_resource_text,(64,9))

    pigsty_hunting_image = [pygame.image.load("hunter_catching1.png"),
                            pygame.image.load("hunter_catching2.png"),
                            pygame.image.load("hunter_catching3.png"),
                            pygame.image.load("hunter_catching4.png"),
                            pygame.image.load("hunter_catching5.png"),
                            pygame.image.load("hunter_catching6.png"),
                            pygame.image.load("hunter_catching7.png"),
                            pygame.image.load("hunter_catching8.png"),
                            pygame.image.load("hunter_catching9.png"),
                            pygame.image.load("hunter_catching10.png")]
    
    if hunting_speed > 0:
        global pigsty1_current
        pigsty1_current =pigsty1_current + hunting_speed/5.0
        if pigsty1_current >= len(pigsty_hunting_image):
            pigsty1_current = 0
        screen.blit(pigsty_hunting_image[int(pigsty1_current)],(162,72))    
    else:
        screen.blit(pygame.image.load("pigsty.png"),(162,72))

#forest1 logging動畫顯示、事件處理
forest1_current = 0
def forest1_logging(logging_speed):

    #wood資源更新
    global wood_resource, logging_level
    wood_resource = logging_level+wood_resource
    wood_resource_text = font.render(f"{wood_resource}", True, (255,255,255))#木頭資源文字物件
    screen.blit(wood_resource_text,(((81 + 81 + 243)/2)+55+2,9))

    forest1_logging_image = [pygame.image.load("logger_working1.png"),
                            pygame.image.load("logger_working2.png"),
                            pygame.image.load("logger_working3.png"),]
    if logging_speed > 0:
        global forest1_current
        forest1_current =forest1_current + logging_speed/5.0
        if forest1_current >= len(forest1_logging_image):
            forest1_current = 0
        screen.blit(forest1_logging_image[int(forest1_current)],(405, 207))    
    else:
        screen.blit(pygame.image.load("forest.png"),(405, 207))

#背景圖片顯示副程式
def image_display():

    #畫面清空
    screen.fill((0,0,0))

    #道路顯示
    screen.blit(Road_image, (81 + 81 + 243, 72 + 27))  #道路1
    screen.blit(Road_image, (81 + 81 + 162, 72 + 27 + 108 + 135))  #道路2
    screen.blit(Road_image, (81 + 81 + 243, 72 + 27 + 108 + 135 + 108 + 135))  #道路3

    #森林顯示
    screen.blit(Forest_image, (81 + 81 + 243, 72 + 27 + 108))
    screen.blit(Forest_image, (81 + 81 + 243, 72 + 27 + 108 + 135 + 108))

    #房子顯示
    screen.blit(House_image, (81 + 81, 72 + 243))

    #空豬圈顯示
    screen.blit(Pigsty_image, (81 + 81, 72))
    screen.blit(Pigsty_image, (81 + 81, 72 + 243 + 162))

    #資源顯示
    #肉
    screen.blit(meat_resource_image,(9,9))

    #木頭
    screen.blit(wood_resource_image,((81 + 81 + 243)/2,9))

    screen.blit(hp_value_image[hp_value-1],(410+350,9))#經驗值
    screen.blit(ex_value_image[ex_value],(410,9))#HP值

    #選單按鈕顯示
    #獵人
    screen.blit(HunterButton_image, (0, 72))
    
    #伐木工
    screen.blit(LoggerButton_image, (81, 72))

    #騎士
    screen.blit(KnightButton_image, (0,170))

#創建 Player 玩家角色
player = Player(350,road_y[1],action="stand") #創建player物件 Player類別
player_road_y = 1 #計算所處道路位置
click_last_time = time.time()#player操作間隔時間計算
player_last_attacked_time = 0
player_level = 0 #player等級

#創建Knight類別清單
knights=[]

#創建Slime類別清單
slimes = []
slimes.append(Slime(1280-108, road_y[random.randint(0, 2)], action="run"))#初始第一隻slime
slime_last_call = time.time() #召喚間隔時間

#創建Dragon類別清單
dragons = []
dragons.append(Dragon(1280-100,road_y[random.randint(0, 2)],action="run"))#初始第一隻dragon
dragons[len(dragons)-1].last_attack_time = time.time() #攻擊間隔時間
dragon_last_call = time.time() #召喚間隔時間

running = True #遊戲循環
clock = pygame.time.Clock()#幀數計算

ex_value = 0 #經驗值
hp_value = len(hp_value_image) #HP值
hp_regenneration = 0 #HP再生

#主程式
if __name__ == "__main__":
    WaitingForGameStart()
    while running:
        #遊戲畫面更新
        screen.fill((0,0,0))#遊戲畫面清空
        image_display()
        forest1_logging(logging_level)
        pigsty1_hunting(hunting_level)
        
        for event in pygame.event.get():#pygame事件輸入
            if event.type == QUIT: 
                running = False#遊戲結束
            #滑鼠點擊事件
            elif event.type == MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                #各項按鈕事件
                if KnightButton_image_rect.collidepoint(mouse_pos):#Knight
                    if meat_resource>500 and wood_resource>500:
                        meat_resource -= 500
                        wood_resource -= 500
                        knights.append(Knight(350,road_y[random.randint(0, 2)],action="run"))
                        knights[len(knights)-1].attack_time = 0
                        print("knight button clicked")
                if HunterButton_image_rect.collidepoint(mouse_pos):#Hunter
                    print(f"hunter button clicked")
                    if ex_value>=5:
                        hunting_level += 1
                        print(f"hunting_level+1 now:{hunting_level}")
                        ex_value-=5
                if LoggerButton_image_rect.collidepoint(mouse_pos):#Logger
                    print(f"logger button clicked")
                    if ex_value >= 5:
                        logging_level += 1
                        print(f"logging_level+1 now:{logging_level}")
                        ex_value-=5
                    
        
        #player事件處理
        if player is player:#player事件處理
            if hp_value <10: #HP小於10時再生
                if (time.time()-hp_regenneration) >3:
                    hp_value += 1
                    hp_regenneration = time.time()
            if hp_value < 1: #HP為0遊戲結束
                running = False    


            keys = pygame.key.get_pressed()#鍵盤讀取
            if keys[pygame.K_UP]:
                if (time.time() - click_last_time) > 0.2: #間隔時間0.2秒
                    player_road_y -= 1
                    player.y = road_y[player_road_y%3]
                    click_last_time = time.time()
            elif keys[pygame.K_DOWN]:
                if (time.time() - click_last_time) > 0.2: #間隔時間0.2秒
                    player_road_y += 1
                    player.y = road_y[player_road_y%3]
                    click_last_time = time.time()
            elif keys[pygame.K_RIGHT]:
                if (time.time() - click_last_time) > 0.2: #間隔時間0.2秒
                    player.action = "run"
                    player.x += 70
                    click_last_time = time.time()
            elif keys[pygame.K_LEFT]:
                if (time.time() - click_last_time) > 0.2: #間隔時間0.2秒
                    player.action = "run"
                    player.x -= 70
                    click_last_time = time.time()
            elif keys[pygame.K_SPACE]:
                if (time.time() - click_last_time) > 0.2: #間隔時間0.2秒
                    player.action = "attack"
                    click_last_time = time.time()
            else:
                player.action = "stand" #無任何事件時 動作為"stand"
            
            player.update()
            player.draw(screen)
            clock.tick(60)

        #所有Slime事件處理
        for slime in slimes:
            # 每 5 秒生成一個新的 Slime
            if len(slimes) < 5: #史萊姆最大數量5
                if (time.time() - slime_last_call) > 3: #間隔時間5秒
                    slimes.append(Slime(1280-100, road_y[random.randint(0, 2)], action="run")) #生成slime到slimes
                    slime_last_call = time.time()  # 更新最後生成時間
            
            if len(slimes) > 0: #如果有slime
                # 出界消失
                if slime.x < (400):   
                   slimes.remove(slime)
                   running = False #game over
                # 被攻擊消失 
                if (slime.y == player.y) and (slime.x < player.x+70) and (slime.x > player.x-10) and player.action == "attack":
                    slimes.remove(slime)
                    if ex_value < len(ex_value_image)-1:# 經驗值增加
                        ex_value += 1
                    if len(slimes) == 0:
                        slimes.append(Slime(1280-100,road_y[random.randint(0, 2)],action="run"))
                # 攻擊player
                if (slime.y == player.y) and (slime.x < player.x+70) and (slime.x > player.x-10) and player.action != "attack":
                    slime.action = "attack"
                    if(time.time() - player_last_attacked_time)>0.5 :
                        player_last_attacked_time = time.time()
                        hp_value -= 1
                #被knight攻擊
                #for knight in knights:
                #    if (knight.y == slime.y) and (slime.x < knight.x+130) and knight.action == "attack":
                #        slimes.remove(slime)
                else:
                    slime.action = "run"
                    slime.x -= 1  # Slime 往左移動

            slime.update()  # 更新 Slime 的動畫
            slime.draw(screen)  # 繪製 Slime

        #所有Dragon事件處理
        for dragon in dragons:
            # 每 5 秒生成一個新的 Dragon
            if len(dragons) < 2: #Dragon最大數量2
                if (time.time() - dragon_last_call) > 5: #間隔時間5秒
                    dragons.append(Dragon(1280-100, road_y[random.randint(0, 2)], action="run")) #生成dragon到dragons
                    dragons[len(dragons)-1].last_attack_time = time.time()
                    dragon_last_call = time.time()  # 更新最後生成時間
            
            if len(dragons) > 0: #如果有dragon
                # 出界消失
                if dragon.x < (100): 
                   dragons.remove(dragon)
                   running = False
                # 被攻擊消失
                if (dragon.y == player.y) and (dragon.x+80  < player.x) and (dragon.x+200 > player.x) and player.action == "attack":
                    dragons.remove(dragon)
                    ex_value += 1
                    if len(dragons) == 0:
                        dragons.append(Slime(1280-100,road_y[random.randint(0, 2)],action="run"))
                        dragons[len(dragons)-1].last_attack_time = time.time()
            # 攻擊player
            if ((time.time() - dragon.last_attack_time) > 5):
                dragon.action = "attack"
                if ((time.time()-dragon.last_attack_time) >7):
                    dragon.last_attack_time = time.time()
                if (player.y == dragon.y) and (player.x+80 > dragon.x) and (dragon.x+300 > player.x):
                    if (time.time()-player_last_attacked_time) >0.5:
                        hp_value -= 1
                        player_last_attacked_time = time.time()
            # 沒有任何條件 往前跑
            else:
                dragon.action = "run"
                dragon.x -= 1
            dragon.update()  # 更新 Dragon 的動畫
            dragon.draw(screen)  # 繪製 Dragon

        #所有Knight事件處理
        for knight in knights:
            #攻擊Slime
            for slime in slimes:
                if (slime.y == knight.y) and (slime.x < knight.x+120):
                    knight.action = "attack"
                    knight.attack_time = time.time()
                    slimes.remove(slime)
                    knight.hp_value -= 1
                    ex_value += 1
                if knight.action == "attack" and time.time() - knight.attack_time < 1:
                    knight.action = "attack"
                else:
                    knight.action = "run"
                    knight.x += 1
            if knight.x > 1280 or knight.hp_value < 1: #出界消失、血量為0消失
                knights.remove(knight)
       
            knight.update()#更新Knight動畫
            knight.draw(screen)#繪製Knight

        pygame.display.flip()  # 畫面更新
        clock.tick(60)  # 設定每秒 60 幀
        screen.fill((0,0,0))#畫面清空
        #=====主迴圈最後一行=====#
    
    # 結束 Pygame
    screen.fill((0,0,0))
    screen.blit(game_over_text,(1280/2-450,720/2-100))
    pygame.display.flip()  # 畫面更新
    time.sleep(3)
    pygame.quit()


"寫完了 謝謝各位"