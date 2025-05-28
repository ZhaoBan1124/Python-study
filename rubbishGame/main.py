import pygame
from pygame.locals import *
from sys import exit
import random
import time

pygame.init()
size = (1000, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("垃圾分类 从我做起！")
backgroundImageFilename = "assets/bg.jpg"
background = pygame.image.load(backgroundImageFilename)
mouseCursorFilename = 'assets/gb.png'
mouseCursor = pygame.image.load(mouseCursorFilename).convert_alpha()


def mouse():
    x, y = pygame.mouse.get_pos()
    pygame.mouse.set_visible(False)
    x -= mouseCursor.get_width() / 2
    y -= mouseCursor.get_height() / 2
    screen.blit(mouseCursor, (x, y))


position = size[0] // 2, size[1] // 2
garbage = [{'img': 'assets/img/1.png', 'key': 0},
           {'img': 'assets/img/2.png', 'key': 1},
           {'img': 'assets/img/3.png', 'key': 1},
           {'img': 'assets/img/4.png', 'key': 3},
           {'img': 'assets/img/5.png', 'key': 0},
           {'img': 'assets/img/6.png', 'key': 0},
           {'img': 'assets/img/7.png', 'key': 3},
           {'img': 'assets/img/8.png', 'key': 3},
           {'img': 'assets/img/9.png', 'key': 3},
           {'img': 'assets/img/10.png', 'key': 0},
           {'img': 'assets/img/11.png', 'key': 2},
           {'img': 'assets/img/12.png', 'key': 1},
           {'img': 'assets/img/13.png', 'key': 0},
           {'img': 'assets/img/14.png', 'key': 0},
           {'img': 'assets/img/15.png', 'key': 1},
           {'img': 'assets/img/16.png', 'key': 1},
           {'img': 'assets/img/17.png', 'key': 0},
           {'img': 'assets/img/18.png', 'key': 1},
           {'img': 'assets/img/19.png', 'key': 2},
           {'img': 'assets/img/20.png', 'key': 2},
           {'img': 'assets/img/21.png', 'key': 2},
           {'img': 'assets/img/22.png', 'key': 0},
           {'img': 'assets/img/23.png', 'key': 2},
           {'img': 'assets/img/24.png', 'key': 3},
           {'img': 'assets/img/25.png', 'key': 0}
           ]
randomNum = random.randint(0, len(garbage) - 1)

rightImg=pygame.image.load('assets/right.png').convert_alpha()
wrongImg=pygame.image.load('assets/wrong.png').convert_alpha()
moving = False
score=0
def judge(key):
    global score,randomNum,position,moving
    if garbage[randomNum]['key'] == key:
        score += 1
        screen.blit(rightImg, (350, 150))
    else:
        screen.blit(wrongImg, (350, 150))
    pygame.display.flip()
    randomNum = random.randint(0, len(garbage) - 1)
    position = size[0] // 2, size[1] // 2
    moving=False
    time.sleep(0.5)
def showText(text,x,y,size):
    fontbigObj=pygame.font.SysFont('SimHei',size)
    screen.blit(fontbigObj.render(text,True,(0,0,0)),(x,y))


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                moving = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                moving = False
        if moving == True:
            position = pygame.mouse.get_pos()
        if 440<=position[1]<=600:
            if 200<=position[0]<=330:
                judge(0)
            elif 350<=position[0]<=480:
                judge(1)
            elif 500 <= position[0] <= 630:
                judge(2)
            elif 650 <= position[0] <= 780:
                judge(3)

    screen.blit(background, (0, 0))
    showText(str(score), 450, 50, 25)
    garbageImg = pygame.image.load(garbage[randomNum]['img']).convert_alpha()
    width, height = garbageImg.get_size()
    screen.blit(garbageImg, (position[0] - width // 2, position[1] - height // 2))
    mouse()
    pygame.display.update()







# import pygame
# from pygame.locals import *
# from sys import exit
# import random
#
#
# pygame.init()
# size=(1000,600)
# screen=pygame.display.set_mode(size)
# pygame.display.set_caption("垃圾分类 从我做起！")
# backgroundImageFilename='assets/bg.jpg'
# background=pygame.image.load(backgroundImageFilename)
# mouseCursorFilename='assets/gb.png'
# mouseCursor=pygame.image.load(mouseCursorFilename).convert_alpha()
#
# def mouse():
#     x,y=pygame.mouse.get_pos()
#     pygame.mouse.set_visible(False)
#     x-=mouseCursor.get_width()/2
#     y-=mouseCursor.get_height()/2
#     screen.blit(mouseCursor,(x,y))
#
# randomNum=random.randint(0,len(garbage)-1)
# garbageImg=pygame.image.load(garbage[randomNum]['img']).concert_alpha()
# while True:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             exit()
#         if event.type==pygame.MOUSEBUTTONDOWN:
#             if event.button==1:
#                 moving=True
#         if event.type==pygame.MOUSEBUTTONUP:
#             if event.button==1:
#                 moving=False
#         if moving==True:
#             position=pygame.mouse.get_pos()
#
#     screen.blit(background,(0,0))
#     mouse()
#     randomNum=random.randint(0,len(garbage)-1)
#
#     width,height=garbageImg.get_size()
#     screen.blit(garbageImg,(position[0]-width//2,position[1]-height//2))
#     pygame.display.update()