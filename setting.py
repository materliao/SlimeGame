import pygame,os #導入所需的函式庫
from pygame.locals import * #導入pygame函式庫

# 1. 取得路徑 (先定義路徑，再使用路徑)
file_path = os.path.abspath(__file__) 
folder_path = os.path.dirname(file_path)
image_path = os.path.join(folder_path, "assets", "image") # 圖片資料夾路徑
font_path = os.path.join(folder_path, "assets", "fonts") # 字體路徑

pygame.init()  #初始化pygame
screen = pygame.display.set_mode((1280, 720)) #設定視窗大小
pygame.display.set_caption("Slime遊戲") #設定視窗標題

road_y = [99,342,585] #道路y座標

#圖片匯入
try:    
    #道路 匯入
    Road_image = pygame.image.load(os.path.join(image_path, "road.png"))
    Road_image_rect = Road_image.get_rect()

    #森林匯入
    Forest_image = pygame.image.load(os.path.join(image_path, "forest.png"))
    Forest_image_rect = Forest_image.get_rect()

    #房子匯入
    House_image = pygame.image.load(os.path.join(image_path, "house.png"))
    House_image_rect = House_image.get_rect()

    #空豬圈匯入
    Pigsty_image = pygame.image.load(os.path.join(image_path, "pigsty.png"))
    Pigsty_image_rect = Pigsty_image.get_rect()

    #資源圖示匯入
    meat_resource_image = pygame.image.load(os.path.join(image_path, "meat_resource_image.png"))#肉
    
    #經驗值圖示匯入
    ex_value_image = [pygame.image.load(os.path.join(image_path, "ex0.png")),
                      pygame.image.load(os.path.join(image_path, "ex1.png")),
                      pygame.image.load(os.path.join(image_path, "ex2.png")),
                      pygame.image.load(os.path.join(image_path, "ex3.png")),
                      pygame.image.load(os.path.join(image_path, "ex4.png")),
                      pygame.image.load(os.path.join(image_path, "ex5.png")),
                      pygame.image.load(os.path.join(image_path, "ex6.png")),
                      pygame.image.load(os.path.join(image_path, "ex7.png")),
                      pygame.image.load(os.path.join(image_path, "ex8.png")),
                      pygame.image.load(os.path.join(image_path, "ex9.png")),
                      pygame.image.load(os.path.join(image_path, "ex10.png")),
                      pygame.image.load(os.path.join(image_path, "ex11.png")),
                      pygame.image.load(os.path.join(image_path, "ex12.png")),
                      pygame.image.load(os.path.join(image_path, "ex13.png")),
                      pygame.image.load(os.path.join(image_path, "ex14.png")),
                      pygame.image.load(os.path.join(image_path, "ex15.png")),
                      pygame.image.load(os.path.join(image_path, "ex16.png")),
                      pygame.image.load(os.path.join(image_path, "ex17.png")),
                      pygame.image.load(os.path.join(image_path, "ex18.png")),
                      pygame.image.load(os.path.join(image_path, "ex19.png")),
                      pygame.image.load(os.path.join(image_path, "ex20.png")),
                      pygame.image.load(os.path.join(image_path, "ex21.png")),]

    #生命值圖示匯入
    hp_value_image = [pygame.image.load(os.path.join(image_path, "hp1.png")),
                      pygame.image.load(os.path.join(image_path, "hp2.png")),
                      pygame.image.load(os.path.join(image_path, "hp3.png")),
                      pygame.image.load(os.path.join(image_path, "hp4.png")),
                      pygame.image.load(os.path.join(image_path, "hp5.png")),
                      pygame.image.load(os.path.join(image_path, "hp6.png")),
                      pygame.image.load(os.path.join(image_path, "hp7.png")),
                      pygame.image.load(os.path.join(image_path, "hp8.png")),
                      pygame.image.load(os.path.join(image_path, "hp9.png")),
                      pygame.image.load(os.path.join(image_path, "hp10.png")),]
    
    #選單按鈕匯入
    #獵人
    HunterButton_image = pygame.image.load(os.path.join(image_path, "hunter_button.png"))
    HunterButton_image_rect = HunterButton_image.get_rect()
    HunterButton_image_rect.topleft = (40,72)
    
except Exception as e:
    print(f"error:{e}")

ex_value = 0 #經驗值
meat_resource = 0 #肉資源

# 創建文字圖像
font = pygame.font.Font(os.path.join(font_path, "Bahnschrift.ttf"), 64)#設定字型和大小（第二個參數是字型大小） None 代表使用 Pygame 預設字型
print(os.path.join(font_path, "Bahnschrift.ttf"))
#(文字內容,抗鋸齒效果,顏色)
def meat_resource_text(txt) :
    return font.render(f"{txt}", True, (255,255,255))#肉資源文字物件
game_over_font = pygame.font.Font(os.path.join(font_path, "Bahnschrift.ttf"), 200)#設定字型和大小
game_over_text = game_over_font.render(f"game over",True,(255,255,255))#遊戲結束文字物件

