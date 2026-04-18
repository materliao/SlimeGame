#stage.py

import pygame,time,random,os,sys
from sprite import *
from setting import *

def waiting_stage_start(now_stage):
    global stage_start  
    waiting=True
    print(f"Stage{now_stage}Start.png")
    start_button_image=pygame.image.load(os.path.join(folder_path+"\\assets\\image\\", f"Stage{now_stage}Start.png"))
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
                    stage_start = True
                    screen.fill((0,0,0))

stage_start = False #預設關卡未開始

stage_run_time = 0 #Stage結束後緩衝時間運算條件
player_last_hurt_time = 0 #玩家受擊冷卻時間

enemy_last_call = 0 #enemy生成間隔時間計算
dragon_last_call = 0  #dragon生成間隔時間計算

enemies = []#儲存敵人清單

#第一關內容 每次生成1隻Slime 任務目標：擊敗5隻
#第一關Slime不會攻擊player
stage1_score = 0
def stage1(player):  
    global stage_start,enemies,stage1_score,stage_run_time,enemy_last_call
    if stage_start != True:
        waiting_stage_start(1)
    else: #stage1主程式
        player.control_event()
        player.draw(screen)
        player.update()
        if stage1_score<5:
            stage_run_time = time.time()
            if (len(enemies) == 0) and (time.time() - enemy_last_call > 2): #生成slime
                enemy_last_call = time.time()
                enemies.append(Slime(1280-108, road_y[random.randint(0, 2)], action="run"))#初始第一隻slime
            for enemy in enemies:
                if enemy.x < 405 or not enemy.alive:
                    enemies.remove(enemy)
                    continue
                else:
                    if (enemy.y == player.y) and (enemy.x < player.x+70) and (enemy.x > player.x-10) and player.action == "attack":
                        stage1_score += 1 
                        enemy.alive = False
                        print("return ex_value_plus")
                        return "ex_value_plus"

                    enemy.x -= 0.5
                    enemy.update()
                    enemy.draw(screen)

        if(time.time() - stage_run_time) > 2.0: #2秒後結束Stage
            enemies.clear()
            stage_start = False
            return "stage1_finish" #結束Stage
            
#第二關內容 每次生成2隻Slime 任務目標：擊敗6隻
#第二關Slime會攻擊player
stage2_score = 0
def stage2(player):
    global stage_start,enemies,stage2_score,stage_run_time,player_last_hurt_time,enemy_last_call
    if stage_start != True:
        waiting_stage_start(2)
    else: #stage2主程式
        player.control_event()
        player.draw(screen)
        player.update()
        if stage2_score<6:
            stage_run_time = time.time()
            if (len(enemies) == 0) and (time.time() - enemy_last_call > 2): #生成slime
                enemy_last_call = time.time()
                enemies.append(Slime(1280-108, road_y[random.randint(0, 2)], action="run"))#初始第一隻slime
                enemies.append(Slime(1280-108, road_y[random.randint(0, 2)], action="run"))#初始第二隻slime
            for enemy in enemies:
                if enemy.x < 405 or not enemy.alive: #移除出界的敵人或死亡的敵人
                    enemies.remove(enemy)
                    continue
                else: #敵人仍在畫面中
                    if (enemy.y == player.y) and (enemy.x < player.x+70) and (enemy.x > player.x-10): 
                        if player.action == "attack": #Slime被攻擊
                            stage2_score += 1 
                            enemy.alive = False
                            print("return ex_value_plus")
                            return "ex_value_plus"
                        else: #Slime攻擊
                            if time.time() - player_last_hurt_time > 0.8: #1秒攻擊冷卻
                                player_last_hurt_time = time.time()
                                enemy.action = "attack"
                                return "hp_value_minus"
                    else:
                        #Slime移動
                        enemy.action = "run"
                        enemy.x -= 0.5
                    enemy.update()
                    enemy.draw(screen)

        if(time.time() - stage_run_time) > 2.0: #2秒後結束Stage
            enemies.clear()
            stage_start = False
            return "stage2_finish" #結束Stage

#第三關內容 每次生成數隻Slime 任務目標：擊敗12隻
#第三關Slime會攻擊player
stage3_score = 0
def stage3(player):
    global stage_start,enemies,stage3_score,stage_run_time,player_last_hurt_time,enemy_last_call
    if stage_start != True:
        waiting_stage_start(3)
    else: #stage3主程式
        player.control_event()
        player.draw(screen)
        player.update()
        if stage3_score<12:
            stage_run_time = time.time()
            if (len(enemies) < 5) and (time.time() - enemy_last_call > 2): #生成slime 每次上限為5
                enemy_last_call = time.time()
                enemies.append(Slime(1280-108, road_y[random.randint(0, 2)], action="run"))#生成slime
            for enemy in enemies:
                if enemy.x < 405 or not enemy.alive: #移除出界的敵人或死亡的敵人
                    enemies.remove(enemy)
                    continue
                else: #敵人仍在畫面中
                    if (enemy.y == player.y) and (enemy.x < player.x+70) and (enemy.x > player.x-10):
                        if player.action == "attack": #Slime被攻擊
                            stage3_score += 1 
                            enemy.alive = False
                            print("return ex_value_plus")
                            return "ex_value_plus"
                        else: #Slime攻擊
                            if time.time() - player_last_hurt_time > 0.8: #1秒攻擊冷卻
                                player_last_hurt_time = time.time()
                                enemy.action = "attack"
                                return "hp_value_minus"
                    else:
                        #Slime移動
                        enemy.action = "run"
                        enemy.x -= 0.5
                    enemy.update()
                    enemy.draw(screen)

        if(time.time() - stage_run_time) > 2.0: #2秒後結束Stage
            enemies.clear()
            stage_start = False
            return "stage3_finish" #結束Stage

#第四關內容 每次生成1隻Dragon 任務目標：擊敗3隻
#第四關Dragon有會攻擊動作
stage4_score = 0
def stage4(player):
    global stage_start,enemies,stage4_score,stage_run_time,dragon_last_call,player_last_hurt_time
    if stage_start != True:
        waiting_stage_start(4)
    else: #stage4主程式
        player.control_event()
        player.draw(screen)
        player.update()
        if stage4_score<3:
            stage_run_time = time.time()
            if (len(enemies) == 0): #生成dragon 每隔5秒才生成一次 每次生成1隻
                if time.time() - dragon_last_call > 5:
                    dragon_last_call = time.time()
                    enemies.append(Dragon(1280-108, road_y[random.randint(0, 2)], action="run"))
            for enemy in enemies:
                if enemy.x < 100 or not enemy.alive: #移除出界的敵人或死亡的敵人
                    enemies.remove(enemy)
                    continue
                if (enemy.y == player.y) and (enemy.x+80  < player.x) and (enemy.x+200 > player.x) and player.action == "attack": #Dragon被攻擊
                    stage4_score += 1 
                    enemy.alive = False
                    return "ex_value_plus"
                elif((time.time() - enemy.last_attack_time) > 5): #Dragon攻擊
                    enemy.action = "attack"
                    if ((time.time()-enemy.last_attack_time) >7):
                        enemy.last_attack_time = time.time()
                    if (player.y == enemy.y) and (player.x+80 > enemy.x) and (enemy.x+300 > player.x):
                        if (time.time()-player_last_hurt_time) >0.5:
                            player_last_hurt_time = time.time()
                            return "hp_value_minus"

                else: #敵人仍在畫面中
                    enemy.action = "run"
                    enemy.x -= 0.5
                enemy.update()
                enemy.draw(screen)

        if(time.time() - stage_run_time) > 2.0: #2秒後結束Stage
            enemies.clear()
            stage_start = False
            return "stage4_finish" #結束Stage

#第五關內容 每次生成n隻Dragon 任務目標：擊敗5隻
#第五關Dragon有會攻擊動作
stage5_score = 0
def stage5(player):
    global stage_start,enemies,stage5_score,stage_run_time,dragon_last_call,player_last_hurt_time
    if stage_start != True:
        waiting_stage_start(5)
    else: #stage5主程式
        player.control_event()
        player.draw(screen)
        player.update()
        if stage5_score<5:
            stage_run_time = time.time()
            if time.time() - dragon_last_call > 5:
                dragon_last_call = time.time()
                for i in range(random.randint(1, 3)):
                    enemies.append(Dragon(1280-108, road_y[random.randint(0, 2)], action="run"))
            for enemy in enemies:
                if enemy.x < 100 or not enemy.alive: #移除出界的敵人或死亡的敵人
                    enemies.remove(enemy)
                    continue
                if (enemy.y == player.y) and (enemy.x+80  < player.x) and (enemy.x+200 > player.x) and player.action == "attack":
                    stage5_score += 1 
                    enemy.alive = False
                    return "ex_value_plus"
                elif((time.time() - enemy.last_attack_time) > 5):
                    enemy.action = "attack"
                    if ((time.time()-enemy.last_attack_time) >7):
                        enemy.last_attack_time = time.time()
                    if (player.y == enemy.y) and (player.x+80 > enemy.x) and (enemy.x+300 > player.x):
                        if (time.time()-player_last_hurt_time) >0.5:
                            player_last_hurt_time = time.time()
                            return "hp_value_minus"

                else: #敵人仍在畫面中
                    enemy.action = "run"
                    enemy.x -= 0.5
                enemy.update()
                enemy.draw(screen)

        if(time.time() - stage_run_time) > 2.0: #2秒後結束Stage
            enemies.clear()
            stage_start = False
            return "stage5_finish" #結束Stage

#第六關內容 每次生成n隻Dragon、Slime 任務目標：共擊敗10隻
#第六關Dragon、Slime都有會攻擊動作
stage6_score = 0
def stage6(player):
    global stage_start,enemies,stage6_score,stage_run_time,dragon_last_call,player_last_hurt_time
    if stage_start != True:
        waiting_stage_start(6)
    else: #stage6主程式
        player.control_event()
        player.draw(screen)
        player.update()
        if stage6_score<10:
            stage_run_time = time.time()
            if time.time() - dragon_last_call > 3:
                dragon_last_call = time.time()
                for i in range(random.randint(1, 3)):
                    if random.randint(0, 1) == 0:
                        enemies.append(Dragon(1280-108, road_y[random.randint(0, 2)], action="run"))
                    else:
                        enemies.append(Slime(1280-108, road_y[random.randint(0, 2)], action="run"))
            for enemy in enemies:
                if enemy.x < 100 or not enemy.alive: #移除出界的敵人或死亡的敵人
                    enemies.remove(enemy)
                    continue
                
                # 判斷敵人種類，以區分受擊與攻擊範圍
                is_dragon = type(enemy) is Dragon
                
                dragon_hitbox = is_dragon and (enemy.x+80 < player.x) and (enemy.x+200 > player.x)
                slime_hitbox = (not is_dragon) and (enemy.x < player.x+70) and (enemy.x > player.x-10)

                # 1. 玩家攻擊判定 (將 Dragon 與 Slime 的受擊邏輯合併)
                if (enemy.y == player.y) and (dragon_hitbox or slime_hitbox) and player.action == "attack":
                    stage6_score += 1 
                    enemy.alive = False
                    if not is_dragon:
                        print("return ex_value_plus") # 保留原本 Slime 特有的 print
                    return "ex_value_plus"
                
                # 2. 怪物攻擊判定 - Dragon 的攻擊邏輯
                elif is_dragon and ((time.time() - enemy.last_attack_time) > 5):
                    enemy.action = "attack"
                    if ((time.time()-enemy.last_attack_time) >7):
                        enemy.last_attack_time = time.time()
                    if (player.y == enemy.y) and (player.x+80 > enemy.x) and (enemy.x+300 > player.x):
                        if (time.time()-player_last_hurt_time) >0.5:
                            player_last_hurt_time = time.time()
                            return "hp_value_minus"

                # 3. 怪物攻擊判定 - Slime 的攻擊邏輯
                elif (not is_dragon) and (enemy.y == player.y) and (enemy.x < player.x+70) and (enemy.x > player.x-10):
                    enemy.action = "attack"
                    if time.time() - player_last_hurt_time > 0.5:
                        player_last_hurt_time = time.time()
                        return "hp_value_minus"
                
                # 4. 敵人移動邏輯 (整合原本重複寫兩次的移動程式碼)
                else: 
                    enemy.action = "run"
                    enemy.x -= 0.5
                
                enemy.update()
                enemy.draw(screen)

        if(time.time() - stage_run_time) > 2.0: #2秒後結束Stage
            enemies.clear()
            stage_start = False
            return "stage6_finish" #結束Stage
#第七關內容 每次生成n隻Dragon、Slime 任務目標：共擊敗15隻
#第七關Dragon、Slime都有會攻擊動作
#第七關開始會有pigsty機制

def stage7(player):
    pass