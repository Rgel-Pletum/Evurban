# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random
import numpy as np
import math
# Цвета (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 255)

BACKGROUND_COL = (0, 200, 0)
TOWN_COL = (0, 0, 0)
ROAD_COL = (255, 0, 0)

TOWN = 40 #количество городов
TRADE_MAX = 18 #интервал ценности торговли
TRADE_MIN = 5

WIDTH = 600  # ширина игрового окна
HEIGHT = 600 # высота игрового окна
FPS = 30 # частота кадров в секунду

def distant(x1,y1,x2,y2):
    dist = int(math.sqrt(((x1-x2)**2)+((y1-y2)**2)))
    return dist



pygame.init()
pygame.mixer.init()  # для звука



screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Evurban")

clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group() 




X = np.random.randint(0,WIDTH,TOWN)
Y = np.random.randint(0,HEIGHT,TOWN)
TRADE = np.random.randint(TRADE_MIN,TRADE_MAX,TOWN)
# Цикл игры
DIST_TABLE = np.zeros((TOWN, TOWN))
for i in range(TOWN):
        for j in range(TOWN):
            DIST_TABLE[i,j] = distant(X[i],Y[i],X[j],Y[j])


WEBROAD = []

for i in range(TOWN):
    flag=0
    ZERO_WEB = np.zeros(TOWN)
    ZERO_WEB[i] = (-1)*distant(0,0,WIDTH,HEIGHT)
    for j in range(TOWN):
        if i != j:
            ZERO_WEB[j] = TRADE[i]*TRADE[j] - DIST_TABLE[i,j]
            if ZERO_WEB[j] > 0:
                ROAD = [i,j]
                flag = 1
                WEBROAD.append(ROAD)
    if  flag == 0:
        ROAD = [i, np.argmax(ZERO_WEB)]
        WEBROAD.append(ROAD)



running = True
while running:
    # Ввод процесса (события)
    # Обновление
    # Визуализация (сборка)
    screen.fill(BACKGROUND_COL)


    for i in range(len(WEBROAD)):
        ROAD=WEBROAD[i]
        X1 = X[ROAD[0]]
        Y1 = Y[ROAD[0]]
        X2 = X[ROAD[1]]
        Y2 = Y[ROAD[1]]
        pygame.draw.line(screen, ROAD_COL, [X1, Y1], [X2, Y2], 2)

    


    for i in range(TOWN):
        pygame.draw.rect(screen, TOWN_COL, (X[i], Y[i], 6,6))
            

    pygame.display.flip()
    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False


    clock.tick(FPS)

pygame.quit()