#sprite.py

import pygame,time,os
from setting import * #設定

#Player類別
class Player:
    def __init__(self, x, y, hp_value,action):
        # player 的位置
        self.x = x
        self.y = y
        self.road_y = 1 #計算所處道路位置,預設在中間道路

        # player 的其他屬性設置
        self.hp = hp_value
        self.ex_value = 0
        self.click_last_time = time.time() #player操作間隔時間計算
        

        # 加載stand和attack和run的圖片
        self.stand_images = [pygame.image.load(os.path.join(folder_path+"\\assets\\image\\", "player_stand.png"))]
        self.attack_images = [pygame.image.load(os.path.join(folder_path+"\\assets\\image\\", "player_attack1.png")), 
                              pygame.image.load(os.path.join(folder_path+"\\assets\\image\\", "player_attack2.png"))]
        self.run_images = [pygame.image.load(os.path.join(folder_path+"\\assets\\image\\", "player_run1.png")),
                           pygame.image.load(os.path.join(folder_path+"\\assets\\image\\", "player_run2.png")),
                           pygame.image.load(os.path.join(folder_path+"\\assets\\image\\", "player_run3.png")),
                           pygame.image.load(os.path.join(folder_path+"\\assets\\image\\", "player_run4.png")),
                           pygame.image.load(os.path.join(folder_path+"\\assets\\image\\", "player_run5.png"))]
        
        # 設定初始圖片與動畫狀態
        self.current_image = 0
        self.animation_speed = 0.3  # 控制動畫速度 數字越大更新越快
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

    def control_event(self): #玩家控制事件處理
        keys = pygame.key.get_pressed()#鍵盤讀取
        if keys[pygame.K_UP]: #上
            if (time.time() - self.click_last_time) > 0.2: #間隔時間0.2秒
                self.road_y -= 1
                self.y = road_y[self.road_y%3]
                self.click_last_time = time.time()
        elif keys[pygame.K_DOWN]: #下
            if (time.time() - self.click_last_time) > 0.2: #間隔時間0.2秒
                self.road_y += 1
                self.y = road_y[self.road_y%3]
                self.click_last_time = time.time()
        elif keys[pygame.K_RIGHT]: #右
            if (time.time() - self.click_last_time) > 0.2: #間隔時間0.2秒
                self.action = "run"
                #self.x += 70
                self.x = min(self.x+70, 1280-100) #限制玩家不超出右邊界
                self.click_last_time = time.time()
        elif keys[pygame.K_LEFT]: #左
            if (time.time() - self.click_last_time) > 0.2: #間隔時間0.2秒
                self.action = "run"
                self.x = max(self.x-70, 81+81+243) #限制玩家不超出左邊界
                self.click_last_time = time.time()
        elif keys[pygame.K_SPACE]: #空格 攻擊
            if (time.time() - self.click_last_time) > 0.2: #間隔時間0.2秒
                self.action = "attack"
                self.click_last_time = time.time()
            if (time.time() - self.click_last_time) > 0.2: #間隔時間0.2秒
                self.action = "attack"
                self.click_last_time = time.time()
        else:
            self.action = "stand" #無任何事件時 動作為"stand"

#Slime類別
class Slime:
    def __init__(self, x, y, action):
        # Slime 的位置
        self.x = x
        self.y = y
        
        self.alive = True #是否需要存在

        # 加載攻擊和奔跑的圖片
        self.attack_images = [pygame.image.load(os.path.join(folder_path+"\\assets\\image\\", "slime_attack1.png")), 
                              pygame.image.load(os.path.join(folder_path+"\\assets\\image\\", "slime_attack2.png"))]
        self.run_images = [pygame.image.load(os.path.join(folder_path+"\\assets\\image\\", "slime_run1.png")),
                           pygame.image.load(os.path.join(folder_path+"\\assets\\image\\", "slime_run2.png")),
                           pygame.image.load(os.path.join(folder_path+"\\assets\\image\\", "slime_run3.png")),
                           pygame.image.load(os.path.join(folder_path+"\\assets\\image\\", "slime_run4.png")),
                           pygame.image.load(os.path.join(folder_path+"\\assets\\image\\", "slime_run5.png"))]
        
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
        self.last_attack_time = time.time()
        self.alive = True #是否需要存在
        # 加載攻擊和奔跑的圖片
        self.attack_images = [pygame.image.load(os.path.join(folder_path+"\\assets\\image\\", "dragon_attack1.png")), 
                              pygame.image.load(os.path.join(folder_path+"\\assets\\image\\", "dragon_attack2.png")),
                              pygame.image.load(os.path.join(folder_path+"\\assets\\image\\", "dragon_attack3.png"))]
        self.run_images = [pygame.image.load(os.path.join(folder_path+"\\assets\\image\\", "dragon_run1.png")),
                           pygame.image.load(os.path.join(folder_path+"\\assets\\image\\", "dragon_run2.png")),
                           pygame.image.load(os.path.join(folder_path+"\\assets\\image\\", "dragon_run3.png")),
                           pygame.image.load(os.path.join(folder_path+"\\assets\\image\\", "dragon_run4.png")),]
        
        # 設定初始圖片與動畫狀態
        self.current_image = 0
        self.animation_speed = 0.1  # 控制動畫速度 數字越大更新越快
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

class Pigsty:
    def __init__(self, x, y,level,action):
        self.x = x
        self.y = y
        self.level = level
        self.action = action
        self.work_images = [pygame.image.load(os.path.join(folder_path+"\\assets\\image\\", "pigsty_work1.png")),
                            pygame.image.load(os.path.join(folder_path+"\\assets\\image\\", "pigsty_work2.png")),
                            pygame.image.load(os.path.join(folder_path+"\\assets\\image\\", "pigsty_work3.png")),
                            pygame.image.load(os.path.join(folder_path+"\\assets\\image\\", "pigsty_work4.png")),
                            pygame.image.load(os.path.join(folder_path+"\\assets\\image\\", "pigsty_work5.png")),
                            pygame.image.load(os.path.join(folder_path+"\\assets\\image\\", "pigsty_work6.png")),
                            pygame.image.load(os.path.join(folder_path+"\\assets\\image\\", "pigsty_work7.png")),
                            pygame.image.load(os.path.join(folder_path+"\\assets\\image\\", "pigsty_work8.png")),
                            pygame.image.load(os.path.join(folder_path+"\\assets\\image\\", "pigsty_work9.png")),
                            pygame.image.load(os.path.join(folder_path+"\\assets\\image\\", "pigsty_work10.png"))]
        self.current_image = 0
        self.animation_speed =  0.1  # 工作動畫速度 隨等級增加而增加
        self.image = self.work_images[self.current_image]
    def update(self):
        if self.action == "work":
            self.current_image += self.animation_speed * self.level #等級越高動畫更新越快
            if self.current_image >= len(self.work_images):
                self.current_image = 0
            self.image = self.work_images[int(self.current_image)]
        else:
            self.image = pygame.image.load(os.path.join(folder_path+"\\assets\\image\\", "pigsty.png"))
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))