import pygame
import sys
import time

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)


def display_FPS(fps):
    fpsFont = pygame.font.Font(None, 40)
    fpsImage = fpsFont.render('%.1f'%fps, True, RED, BLUE)
    screen.blit(fpsImage, (0,0))
    

def main():
    width = 1024 # 窗口宽度
    height = 576 # 窗口高度
    FPS = 30 # 画面帧率

    pygame.init() # 初始化pygame
    pygame.mixer.init() # 初始化音效库

    global screen
    screen = pygame.display.set_mode((width, height), 0, 32)
    pygame.display.set_caption("display FPS")

    clock = pygame.time.Clock() # 获取 clock 对象

    running = True
    while running:
        clock.tick(FPS) # 控制窗口刷新速度
        # 获取事件并逐类响应
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        # 绘制与渲染
        screen.fill((0,0,0))
        display_FPS(clock.get_fps()) # 在屏幕上显示帧率
        # 更新屏幕
        pygame.display.update()
        
                
    pygame.quit()
    
    
if __name__ == "__main__":
    main()
    sys.exit()