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
        self.base_speed = base_speed
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

    def exterminatus(self, event):
        x_pos, y_pos = event.pos
        if (x_pos - self.coord[0])**2 + (y_pos - self.coord[1])**2 <= (self.r)**2:
            self.life = False


class Fireworks:

    def __init__(self, start_rad, start_place, start_speed, start_a, start_color, start_number):
        self.rad = start_rad
        self.place = start_place
        self.speed = start_speed
        self.a = start_a
        self.color = start_color
        self.number = start_number
        self.x = self.creating()[0]
        self.y = self.creating()[1]
        self.vx = self.creating()[2]
        self.vy = self.creating()[3]
        self.timelife = 0

    def creating(self):
        vx = []
        vy = []
        x = []
        y = []
        alfa0 = randint(0, int(360/self.number))
        for num in range(self.number):
            x.append(self.place[0])
            y.append(self.place[1])
            vx.append(self.speed * sin(alfa0 + 360 * num / self.number))
            vy.append(self.speed * cos(alfa0 + 360 * num / self.number))
        return [x, y, vx, vy]

    def move(self):
        for num in range(self.number):
            self.x[num] = self.x[num] + self.vx[num]
            self.y[num] = self.y[num] + self.vy[num]
            self.vy[num] = self.vy[num] + self.a

    def draw(self):
        for num in range(self.number):
            lifefactor = -0.1 * self.speed + 3.4
            circle(screen, self.color, [self.x[num], self.y[num]], self.rad - self.timelife/lifefactor)
        self.timelife = self.timelife + 1


def printer(title, valye, text_size=100, base_coords=(10, 10)):
    font = pygame.font.Font(None, text_size)
    text = font.render(title, True, [255, 255, 255])
    screen.blit(text, base_coords)
    text = font.render(str(valye), True, [255, 255, 255])
    screen.blit(text, (base_coords[0], base_coords[1]+text_size+20))

counter_devil = 1
antiscore = -5.
new_balls = 0
lifes_default = 8.
lifes = int(lifes_default)

pool = []
for VoVa in range(10):
    pool.append(Ball(base_r=20+2*VoVa))

pool2 =[]

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)

    first_lifes = lifes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            lives_per_event = 0
            for ball in pool:
                ball.exterminatus(event)
                if ball.life == False:
                    rad = ball.r * 1/2
                    place = ball.coord
                    base_speed = ball.base_speed
                    a = randint(1, 4)
                    color = ball.color
                    number = randint(4, 9)
                    pool.pop(pool.index(ball))
                    pool2.append(Fireworks(rad, place, base_speed, a, color, number))
                    lives_per_event += len(pool) + 2
                    if new_balls > 1:
                        counter_devil -= 10
                else:
                    lives_per_event -= 1
            print('l:', lives_per_event)
            lifes += lives_per_event

    for ball in pool:
        if counter_devil == 100:
            min_r, max_r = 22, 30
            min_s, max_s = 18, 24
            b_r = randint(min_r, max_r)
            b_s = randint(min_s, max_s)
            pool.append(Ball(base_r=b_r, base_speed=b_s))
            counter_devil = 1
            range_antiscore = 4*(b_r-min_r)**2/(max_r-min_r)**2 + (max_s-b_s)/(max_s-min_s)
            antiscore += range_antiscore
            new_balls += 1
        ball.draw()
        ball.collision()
        ball.move()

    for fire in pool2:
        fire.draw()
        fire.move()

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
    if lifes == 0:
        pool.clear()
        antiscore = 100.

    printer("0ставшиеся жизни", lifes, 40)

    counter_devil += 1
    pygame.display.update()
    screen.fill((0, 0, 0))

print("antiscore, new_balls \n", antiscore, new_balls)

pygame.quit()

