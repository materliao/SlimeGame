import pygame
import sys

# 初始化 Pygame
pygame.init()

# 设置屏幕
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame 显示文字示例")

# 定义字体和文字内容
font = pygame.font.Font(None, 50)  # 使用默认字体，字号50
text_surface = font.render("你好，Pygame！", True, (255, 255, 255))  # 白色文字

# 设置文字位置
text_rect = text_surface.get_rect(center=(400, 300))

# 主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 绘制背景和文字
    screen.fill((0, 0, 0))  # 黑色背景
    screen.blit(text_surface, text_rect)  # 绘制文字

    # 更新屏幕
    pygame.display.flip()
