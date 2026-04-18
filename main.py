#main.py

import pygame,time,os #導入所需的函式庫
from pygame.locals import * #導入pygame函式庫
from setting import * #設定
from sprite import * #角色類別
from stage import * #關卡函式

pygame.init()  #初始化pygame

player = Player(350,road_y[1],len(hp_value_image),action="stand") #玩家角色物件
hp_regenneration = time.time() #hp再生計算

running = True #遊戲運行狀態
clock = pygame.time.Clock()#幀數計算

#背景圖片顯示副程式
def image_display():
    screen.fill((0,0,0))#畫面清空

    #背景色塊顯示 RGB(190,234,208)
    pygame.draw.rect(screen,(190,234,208),(81+81-10,72-10,1280,720))

    #道路顯示
    screen.blit(Road_image, (81 + 81 + 243, 72 + 27))  #道路1
    screen.blit(Road_image, (81 + 81 + 162, 72 + 27 + 108 + 135))  #道路2
    screen.blit(Road_image, (81 + 81 + 243, 72 + 27 + 108 + 135 + 108 + 135))  #道路3

    #森林顯示
    screen.blit(Forest_image, (81 + 81 + 243, 72 + 27 + 108-25))
    screen.blit(Forest_image, (81 + 81 + 243, 72 + 27 + 108 + 135 + 108-25))

    #空豬圈顯示
    screen.blit(Pigsty_image, (81 + 81, 72))
    screen.blit(Pigsty_image, (81 + 81, 72 + 243 + 162))

    #房子顯示
    screen.blit(House_image, (81 + 81+5, 72 + 243-20))

    #資源顯示
    #肉
    screen.blit(meat_resource_image,(9,9))
    screen.blit(meat_resource_text,(9+54+2,9))

    #木頭
    screen.blit(wood_resource_image,((81 + 81 + 243)/2,9))
    screen.blit(wood_resource_text,(((81 + 81 + 243)/2)+55+2,9))
    
    screen.blit(hp_value_image[player.hp-1],(410+350,9))#經驗值
    screen.blit(ex_value_image[player.ex_value],(410,9))#HP值

    #選單按鈕顯示
    #獵人
    screen.blit(HunterButton_image, (0, 72))
    
    #伐木工
    screen.blit(LoggerButton_image, (81, 72))

stage = 5 #初始關卡等級
stage_start = False #預設關卡未開始

#主程式
if __name__ == "__main__":
    print("Game Start")
    
    while running and player.hp > 0:
        for event in pygame.event.get():#pygame事件輸入
            if event.type == QUIT: 
                running = False#遊戲結束
            #滑鼠點擊事件
            elif event.type == MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                
                
                if HunterButton_image_rect.collidepoint(mouse_pos): #點擊獵人按鈕
                    print("hunter button clicked")

        image_display()#背景圖片顯示

        #hp再生,每4秒回復1點hp
        if (player.hp<10) and (time.time()-hp_regenneration>4):
            print("hp plus")
            player.hp += 1
            hp_regenneration = time.time() 

        match stage: #關卡判斷
            case 1: #第一關
                stage_result = stage1(player)
                if stage_result == "stage1_finish":stage += 1 #結束第一關
                elif stage_result == "ex_value_plus": #增加經驗值
                    player.ex_value = min(player.ex_value + 1, len(ex_value_image)-1)
            case 2: #第二關
                stage_result = stage2(player)
                if stage_result == "stage2_finish":stage += 1 #結束第二關
                elif stage_result == "ex_value_plus": #增加經驗值
                    player.ex_value = min(player.ex_value + 1, len(ex_value_image)-1)
                elif stage_result == "hp_value_minus": #減少生命值
                    player.hp -= 1
            case 3: #第三關
                stage_result = stage3(player)
                if stage_result == "stage3_finish":stage += 1 #結束第三關
                elif stage_result == "ex_value_plus": #增加經驗值
                    player.ex_value = min(player.ex_value + 1, len(ex_value_image)-1)
                elif stage_result == "hp_value_minus": #減少生命值
                    player.hp -= 1
            case 4: #第四關
                stage_result = stage4(player)
                if stage_result == "stage4_finish":stage += 1 #結束第四關
                elif stage_result == "ex_value_plus": #增加經驗值
                    player.ex_value = min(player.ex_value + 1, len(ex_value_image)-1)
                elif stage_result == "hp_value_minus": #減少生命值
                    player.hp -= 1
            case 5: #第五關
                stage_result = stage5(player)
                if stage_result == "stage5_finish":stage += 1 #結束第五關
                elif stage_result == "ex_value_plus": #增加經驗值
                    player.ex_value = min(player.ex_value + 1, len(ex_value_image)-1)
                elif stage_result == "hp_value_minus": #減少生命值
                    player.hp -= 1
            case 6: #第六關
                stage_result = stage6(player)
                if stage_result == "stage6_finish":stage += 1 #結束第六關
                elif stage_result == "ex_value_plus": #增加經驗值
                    player.ex_value = min(player.ex_value + 1, len(ex_value_image)-1)
                elif stage_result == "hp_value_minus": #減少生命值
                    player.hp -= 1
        pygame.display.flip()  # 畫面更新
        clock.tick(60)  # 設定每秒 60 幀
    
    #遊戲結束
    screen.fill((0,0,0))#畫面清空
    screen.blit(game_over_text,(1280/2-450,720/2-100))
    pygame.display.flip()  # 畫面更新
    time.sleep(0.5)
    pygame.quit()
