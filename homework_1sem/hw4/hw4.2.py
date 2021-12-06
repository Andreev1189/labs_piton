from operator import index

import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 400))

#                RGB          x'   y'   lx  ly, weight
# rect(screen, (0, 0, 255), (100, 100, 200, 200), 0)
#                     RGB         dot1      dot2      dot3    ....          weight
# polygon(screen, (255, 255, 0), [(0, 0), (100, 50), (300, 100), (100, 100)], 1)
#                   RGB         Ox, Oy     R  weight
# circle(screen, (0, 255, 0), (200, 175), 100, 1)

rect(screen, (76, 241, 252), (0, 0, 700, 180), 0)
rect(screen, (31, 94, 255), (0, 180, 700, 100), 0)
rect(screen, (255, 231, 18), (0, 280, 700, 120), 0)     #ukraine

circle(screen, (255, 231, 18), (535, 55), 35, 0)        #sun

for i in range(14):
    if (-1)**i == 1:
        circle(screen, (31, 94, 255), ((25+50*i), (280 - (-1)**i*25)), 35, 0)
    if (-1)**i == -1:
        circle(screen, (255, 231, 18), ((25+50*i), (280 - (-1)**i*25)), 35, 0)

o6JIaka_0 = [(132, 47), (120, 60), (151, 49), (139, 63), (160, 62), (170, 50), (177, 63)]
for cloud in o6JIaka_0:
    circle(screen, (255, 255, 255), cloud, 12, 0)
    circle(screen, (55, 55, 55), cloud, 12, 1)

o6JIaka_1 = []
for cloud in o6JIaka_0:
    c0 = cloud[0] - 40
    c1 = cloud[1] + 60
    o6JIaka_1.append((c0, c1))
for cloud in o6JIaka_1:
    circle(screen, (255, 255, 255), cloud, 15, 0)
    circle(screen, (55, 55, 55), cloud, 15, 1)

o6JIaka_2 = []
for cloud in o6JIaka_0:
    c0 = cloud[0] + 140
    c1 = cloud[1] + 40
    o6JIaka_2.append((c0, c1))
for cloud in o6JIaka_2:
    circle(screen, (255, 255, 255), cloud, 11, 0)
    circle(screen, (55, 55, 55), cloud, 11, 1)

polygon(screen, (224, 161, 0), [(90, 233), (96, 233), (96, 383), (90, 383)], 0)
polygon(screen, (255, 0, 170), [(90, 233), (26, 263), (162, 263), (96, 233)], 0)
_3oHT1_ = [26, 41, 61, 80, 90]
_3oHT2_ = [96, 108, 127, 147, 162]
for dot in _3oHT1_:
    polygon(screen, (55, 55, 55), [(90, 233), (dot, 263), (90, 233)], 1)
for dot in _3oHT2_:
    polygon(screen, (55, 55, 55), [(96, 233), (dot, 263), (96, 233)], 1)

def sector(X0, Y0, R):
    koords = []
    for kX in range(X0-R, X0):
        y = Y0 + (R**2 - (kX-X0)**2)**(1/2)
        koords.append((kX, y))
    koords.append((X0, Y0))
    polygon(screen, (255, 153, 0), koords, 0)


sector(352, 205, 30)     # KopMa
polygon(screen, (255, 153, 0), [(352, 205), (559, 205), (495, 235), (352, 235)], 0)   # 6opT
circle(screen, (255, 255, 255), (509, 216), 7, 0)
circle(screen, (0, 0, 0), (509, 216), 7, 2)           # okHo
polygon(screen, (0, 0, 0), [(405, 206), (410, 206), (410, 110), (405, 110)], 0)  # Ma4Ta
# napyc:
polygon(screen, (200, 200, 200), [(467, 157), (427, 157), (410, 110), (467, 157), (410, 206), (427, 157)], 0)
polygon(screen, (0, 0, 0), [(467, 157), (427, 157), (410, 110), (467, 157), (410, 206), (427, 157)], 1)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()