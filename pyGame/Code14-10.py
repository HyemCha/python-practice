import pygame
import random
import sys

# 함수 선언부분

def playGame():
    global monitor
    r = random.randrange(0,256)
    g = random.randrange(0,256)
    b = random.randrange(0,256)

    while True:
        (pygame.time.Clock()).tick(50)
        monitor.fill(r, g, b) # 화면 배경 칠하기

        # 키보드 또는 마우스 이벤트 들어오는지 체크
        for e in pygame.event.get():
            if e.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        print('~', end='')

# 전역 변수 선언
r, g, b = [0]*3
swidth, sheight = 500, 700
monitor = None

# 메인
pygame.init()
monitor = pygame.display.set_mode((swidth, sheight))
pygame.display.set_caption('우주괴물 무찌르기')

playGame()