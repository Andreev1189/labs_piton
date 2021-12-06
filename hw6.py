import pygame
from pygame.draw import *
from random import randint
from math import *
pygame.init()

FPS = 30
BORDERS = (1200, 900)
screen = pygame.display.set_mode(BORDERS)


class Ball:

    def __init__(self, base_speed=10, base_r=30):
        self.coord = [randint(50, BORDERS[0] - 50), randint(50, BORDERS[1] - 50)]
        alfa = randint(0, 360)
        self.speed = [cos(alfa)*base_speed, sin(alfa)*base_speed]
        self.color = self.make_color()
        self.r = base_r
        self.life = True

    def make_color(self):
        color = []
        a = randint(150, 250)
        b = randint(100, 150)
        c = randint(0, 50)
        help_randint = [a, b, c]
        c1_num = randint(0, 2)
        color.append(help_randint[c1_num])
        help_randint.pop(c1_num)
        c2_num = randint(0, 1)
        color.append(help_randint[c2_num])
        help_randint.pop(c2_num)
        color.append(help_randint[0])
        color = tuple(color)
        return color

    def move(self):
        self.coord[0] += self.speed[0]
        self.coord[1] += self.speed[1]

    def draw(self):
        circle(screen, self.color, self.coord, self.r)

    def collision(self):
        if self.coord[0] - self.r <= 0 or self.coord[0] + self.r >= BORDERS[0]:
            self.speed[0] *= -1
        if self.coord[1] - self.r <= 0 or self.coord[1] + self.r >= BORDERS[1]:
            self.speed[1] *= -1

    def exterminatus(self):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (event.pos[0] - self.coord[0])**2 + (event.pos[1] - self.coord[1])**2 <= (self.r)**2:
                self.life = False


counter_devil = 1
antiscore = -5.
new_balls = 0
lifes_default = 42.
lifes = int(lifes_default)

pool = []
for VoVa in range(10):
    pool.append(Ball(base_r=10+2*VoVa))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)

    first_lifes = lifes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    for ball in pool:
        if counter_devil == 90:
            min_r, max_r = 18, 26
            min_s, max_s = 18, 24
            b_r = randint(min_r, max_r)
            b_s = randint(min_s, max_s)
            pool.append(Ball(base_r=b_r, base_speed=b_s))
            counter_devil = 1
            range_antiscore = 4*(b_r-min_r)**2/(max_r-min_r)**2 + (max_s-b_s)/(max_s-min_s)
            antiscore += range_antiscore
            new_balls += 1
        Ball.draw(ball)
        Ball.collision(ball)
        Ball.move(ball)
        if event.type == pygame.MOUSEBUTTONDOWN:
            Ball.exterminatus(ball)
            if ball.life == False:
                pool.pop(pool.index(ball))
                lifes += len(pool) + 2
                if new_balls > 1:
                    counter_devil -= 10
            else:
                lifes += -1

    if len(pool) == 0:
        font = pygame.font.Font(None, 100)
        text = font.render(str(int(100. - antiscore)), True, [255, 255, 255])
        screen.blit(text, (325, 200))
        text = font.render("TBou pe3yJIbTaT:", True, [255, 255, 255])
        screen.blit(text, (100, 100))
        text = font.render(".", True, [255, 255, 255])
        screen.blit(text, (249, 63))

    if lifes > first_lifes:
        lifes = int(lifes_default)
        print(lifes)
    if lifes < first_lifes:
        lifes += len(pool) - 1
        print(lifes)
    if lifes < 0:
        pool.clear()
        antiscore = 100.
    counter_devil += 1
    pygame.display.update()
    screen.fill((0, 0, 0))

print("antiscore, new_balls \n", antiscore, new_balls)

pygame.quit()

