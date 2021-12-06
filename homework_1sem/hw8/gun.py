import math
from pygame.draw import *
from random import choice, randint

import pygame

k = 6
FPS = 30*k

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600
BORDERS = [WIDTH, HEIGHT]


class Ball:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.a = 2/k**2
        self.color = choice(GAME_COLORS)
        self.live = 30
        self.lifecheck = 0

    def move(self):
        self.x += self.vx
        self.y -= self.vy
        self.vy -= self.a

    def collision(self):
        if self.x + self.r + self.vx >= BORDERS[0]:
            self.vx *= -0.7
            self.vy *= 0.7
            self.x = BORDERS[0] - self.r - 1
        if self.x - self.r + self.vx <= 0:
            self.vx *= -0.7
            self.vy *= 0.7
            self.x = 0 + self.r + 1
        if self.y + self.r - self.vy >= BORDERS[1]:
            self.vy *= -0.7
            self.vx *= 0.7
            self.y = BORDERS[1] - self.r
            if self.vy < 3 * self.a:
                self.lifecheck += 1

    def collision_choice(self):
        if self.x - self.r + self.vx <= 0 or self.x + self.r + self.vx >= BORDERS[0]:
            return False
        if self.y + self.r - self.vy >= BORDERS[1]:
            return False
        else:
            return True

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)

    def hittest(self, obj):
        if (obj.x - self.x)**2 + (obj.y - self.y)**2 <= (self.r + obj.r)**2:
            return True
        else:
            return False


class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10/k
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.x, self.y = 20, 450
        self.flag_k_left, self.flag_k_right, self.flag_k_up, self.flag_k_down = False, False, False, False

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """
        Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen, x=self.x, y=self.y)
        new_ball.r += 5
        if event.pos[0] != self.x:
            self.an = math.atan((event.pos[1] - self.y) / (event.pos[0] - self.x))
        new_ball.vx = self.f2_power * (math.cos(self.an))
        new_ball.vy = - self.f2_power * (math.sin(self.an))
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10/k

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event and (event.pos[0]-self.x) != 0:
            self.an = math.atan((event.pos[1] - self.y) / (event.pos[0] - self.x))
        if (event.pos[0]-self.x) == 0:
            self.an = 90
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self, color):
        polygon(screen, color,
                [(self.x, self.y), (self.x + (self.f2_power+10) * math.cos(self.an), self.y + (self.f2_power+10) * math.sin(self.an)), (self.x, self.y)],
                5)

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 2/k**2
            self.color = RED
        else:
            self.color = GREY

    def move_check(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.flag_k_left = True
            if event.key == pygame.K_RIGHT:
                self.flag_k_right = True
            if event.key == pygame.K_UP:
                self.flag_k_up = True
            if event.key == pygame.K_DOWN:
                self.flag_k_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.flag_k_left = False
            if event.key == pygame.K_RIGHT:
                self.flag_k_right = False
            if event.key == pygame.K_UP:
                self.flag_k_up = False
            if event.key == pygame.K_DOWN:
                self.flag_k_down = False

    def move(self):
        move_value = 1
        if self.flag_k_left:
            self.x -= move_value
        if self.flag_k_right:
            self.x += move_value
        if self.flag_k_up:
            self.y -= move_value
        if self.flag_k_down:
            self.y += move_value


class Target:

    def __init__(self, screen):
        target_info = self.new_target()
        self.x = target_info[0]
        self.y = target_info[1]
        self.r = target_info[2]
        self.color = target_info[3]
        self.screen = screen

    def new_target(self):
        """ Инициализация новой цели. """
        x = randint(600, 780)
        y = randint(300, 550)
        r = randint(2, 50)
        color = RED
        return [x, y, r, color]

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []

clock = pygame.time.Clock()
gun = Gun(screen)
target = []
target.append(Target(screen))

finished = False

while not finished:
    screen.fill(WHITE)
    gun.draw((0, 0, 0))
    gun.move()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            gun.draw((200, 200, 0))
        else:
            gun.draw((0, 0, 0))
    for t in target:
        t.draw()
    for b in balls:
        if b.collision_choice():
            b.move()
        else:
            b.collision()
            if b.lifecheck > 8:
                balls.pop(balls.index(b))
        b.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            gun.move_check(event)
        elif event.type == pygame.MOUSEBUTTONDOWN and len(target) != 0:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP and len(target) != 0:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    for b in balls:
        for t in target:
            if b.hittest(t):
                target.pop(target.index(t))

    if len(target) == 0 and len(balls) == 0:
        target.append(Target(screen))

    gun.power_up()

pygame.quit()
