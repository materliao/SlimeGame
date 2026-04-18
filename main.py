#main.py

import pygame,time,os #導入所需的函式庫
from pygame.locals import * #導入pygame函式庫
from setting import * #設定
from sprite import * #角色類別
from stage import * #關卡函式

pygame.init()  #初始化pygame

player = Player(81+81+243,road_y[1],len(hp_value_image),action="stand") #玩家角色物件
hp_regenneration = time.time() #hp再生計算

pigsty1 = Pigsty(81+81,72,0,"not_work") #豬圈1物件
pigsty2 = Pigsty(81+81,72+243+162,0,"not_work") #豬圈2物件

#資源數量
meat_resource = 0 #肉

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

    #豬圈顯示
    pigsty1.update()
    pigsty1.draw(screen)
    pigsty2.update()
    pigsty2.draw(screen)

    #房子顯示
    screen.blit(House_image, (81 + 81+5, 72 + 243-20))

    #資源顯示
    #肉
    screen.blit(meat_resource_image,(9,9))
    screen.blit(meat_resource_text(int(meat_resource)),(9+54+2,9))
    
    screen.blit(hp_value_image[player.hp-1],(410+350,9))#經驗值
    screen.blit(ex_value_image[player.ex_value],(410,9))#HP值

    #選單按鈕顯示
    #獵人
    screen.blit(HunterButton_image, (40, 72))

stage = 1 #初始關卡等級
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
                    if player.ex_value >= 5: #如果經驗值足夠
                        if pigsty1.action == "not_work": #如果豬圈1沒在工作
                            player.ex_value -= 5 #扣除經驗值
                            pigsty1.action = "work" #豬圈1開始工作
                            pigsty1.level += 1 #豬圈1等級提升
                            print("Hunter Button Clicked, Pigsty1 launch, Level:", pigsty1.level)
                        else: #如果豬圈1已經在工作
                            if pigsty2.action == "not_work": #如果豬圈2沒在工作
                                player.ex_value -= 5 #扣除經驗值
                                pigsty2.action = "work" #豬圈2開始工作
                                pigsty2.level += 1 #豬圈2等級提升
                                print("Hunter Button Clicked, Pigsty2 launch, Level:", pigsty2.level)
                            else: #如果豬圈2也在工作
                                pigsty1.level += 1 #豬圈1等級提升
                                pigsty2.level += 1 #豬圈2等級提升
                                print("Hunter Button Clicked, Both Pigsty level up, Pigsty1 Level:", pigsty1.level, "Pigsty2 Level:", pigsty2.level)

                    else:
                        print("Hunter Button Clicked, but not enough experience!")

        image_display()#背景圖片顯示

        #hp再生,每4秒回復1點hp
        if (player.hp<10) and (time.time()-hp_regenneration>4):
            print("hp plus")
            player.hp += 1
            hp_regenneration = time.time() 

        meat_resource += 0.1*pigsty1.level + 0.1*pigsty2.level

        match stage: #關卡判斷
            case 1: #第一關
                stage_result = stage1(player)
                if stage_result == "stage1_finish":stage += 1 #結束第一關
                elif stage_result == "ex_value_plus": #增加經驗值
                    player.ex_value = min(player.ex_value + 1, len(ex_value_image)-1)
                    print("ex_value:",player.ex_value)
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