import pygame
import random
import sqlite3
import sys
from os import path
import os
if getattr(sys, 'frozen', False):
    CurrentPath = sys._MEIPASS
else:
    CurrentPath = os.path.dirname(__file__)
WIDTH = 1500
HEIGHT = 800
FPS = 60
connection= sqlite3.connect('pygame.db')
cursor = connection.cursor()
pygame.init()
GREEN = (0, 255, 0)
BLACK=(0,0,0)
screen = pygame.display.set_mode((WIDTH, HEIGHT),pygame.DOUBLEBUF |pygame.SCALED|pygame.FULLSCREEN)
pygame.mixer.init()
pygame.display.set_caption('Qubik-Rubick')
spriteFolderPath = path.join(CurrentPath, 'sprites')
bg11 = os.getcwd()
bg15 = bg11+'\sprites/1233.bmp'
pygame.display.set_icon(pygame.image.load(path.join(spriteFolderPath, bg15)))
clock = pygame.time.Clock()
cvet = 0
txt = pygame.font.SysFont('arial', 36)
ground = HEIGHT-70
color = (0, 128, 255)
p = 4
a = 60
cursor.execute('''
CREATE TABLE IF NOT EXISTS score (
score INTEGER PRIMARY KEY,
id INTEGER NOT NULL
)
''')
connection.commit()
b = 60
bg13 = bg11+'\sprites/1111.jpg'
bg12 = bg11+'\sprites/1000.jpeg'
bg = pygame.image.load(path.join(spriteFolderPath, bg13))
bg2 = pygame.image.load(path.join(spriteFolderPath, bg12))
score = 0
jump_force = 5
move = jump_force+1
qqqqq = True
while qqqqq:
    o = False
    qqq1 = random.randint(300, 600)
    poy1 = random.randint(0, 350)
    qqq2 = random.randint(300, 600)
    poy2 = random.randint(0, 350)
    qqq3 = random.randint(300, 600)
    poy3 = random.randint(0, 350)
    xd1 = WIDTH
    xd2 = WIDTH+500
    xd3 = WIDTH+1000
    x = 0
    y = HEIGHT/2
    ochki = 0
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_SPACE]:
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    cvet = 1
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    run = False
                    qqqqq = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                        o = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_v:
                        o = False
            if not(o):
                a2 = txt.render('Ваши очки: ' + str(ochki), True, (0, 0, 0))
                screen.blit(bg2, (0, 0))
                screen.blit(a2, (WIDTH / 2 - 50, 0))
                kub = pygame.Rect(x, y, 60, 60)
                pygame.draw.rect(screen, color, kub)
                prep1 = pygame.Rect(xd1, poy1, 25, qqq1)
                pygame.draw.rect(screen, (0, 0, 0), prep1)
                if xd1 - 2 <= 0:
                    xd1 = WIDTH
                    qqq1 = random.randint(300, 600)
                    poy1 = random.randint(0, 350)
                    ochki += 50
                else:
                    xd1 -= 5
                prep2 = pygame.Rect(xd2, poy2, 25, qqq2)
                pygame.draw.rect(screen, (0, 0, 0), prep2)
                if xd2 - 2 <= 0:
                    xd2 = WIDTH
                    qqq2 = random.randint(300, 600)
                    poy2 = random.randint(0, 350)
                    ochki += 50
                else:
                    xd2 -= 5
                prep3 = pygame.Rect(xd3, poy3, 25, qqq3)
                pygame.draw.rect(screen, (0, 0, 0), prep3)
                if xd3 - 2 <= 0:
                    xd3 = WIDTH
                    qqq3 = random.randint(300, 600)
                    poy3 = random.randint(0, 350)
                    ochki += 50
                else:
                    xd3 -= 5
                clock.tick(FPS)
                pygame.display.flip()
                if pygame.Rect.colliderect(kub, prep1) or pygame.Rect.colliderect(kub, prep2) or pygame.Rect.colliderect(kub, prep3):
                    run = False
                    try:
                        cursor.execute('INSERT INTO score (score,id) VALUES (?,?)',(ochki,random.randint(1,1000000000000000)))
                        connection.commit()
                    except sqlite3.IntegrityError:
                        pass
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_w] and y>0 : y -= p
                if pressed[pygame.K_s] and y < HEIGHT-b : y += p
                if pressed[pygame.K_a] and x>0 : x -= p
                if pressed[pygame.K_d] and x<WIDTH-a: x += p
                if pressed[pygame.K_UP]and y>0 : y -= p
                if pressed[pygame.K_DOWN]and y < HEIGHT-b : y += p
                if pressed[pygame.K_LEFT]and x>0 : x -= p
                if pressed[pygame.K_RIGHT]and x<WIDTH-a: x += p
                screen.fill(GREEN)
                screen.blit(bg, (0, 0))
                if cvet ==0:
                    color = (0, 128, 255)
                elif cvet ==1:
                    color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
                    cvet=2
                colorb  = (0,0,0)
            else:
                pygame.display.flip()
                screen.fill((255, 255, 255))
                a2 = txt.render('Чтобы продолжить игру нажмите v.', True, (0, 0, 0))
                screen.blit(a2, (500, HEIGHT / 2))
    else:
        cursor.execute('SELECT * FROM score')
        sc = cursor.fetchall()
        try:
            score = max(sc)
            score1 = score[0]
        except ValueError:
            score1 = 0
        a1 = txt.render('Чтобы начать игру нажмите SPACE.', True, (0, 0, 0))
        a3 = txt.render('Чтобы выйти из игры,нажмите esc,для паузы нажмите P!Для её возобновления нажмите v',True, (0, 0, 0))
        a4 = txt.render('Ваш рекорд:'+str(score1),True, (0, 0, 0))
        screen.blit(bg,(0,0))
        screen.blit(a1, (500,HEIGHT/2-60))
        screen.blit(a3, (150, HEIGHT / 2))
        screen.blit(a4, (600, HEIGHT / 2+60))
        pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            qqqqq = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            qqqqq = False
connection.close()
pygame.quit()