import turtle
from random import *
from random import randint
from math import cos

print('A' + 'BOBA')



# 4 napa6oJIa

turtle.penup()
x = 0
y = 0
Vx = 10
Vy = 50
ay = -10
dt = 1
for VoVa in range(1000):
    x += Vx * dt
    y += Vy * dt + ay * dt ** 2 / 2
    Vy += ay * dt
    turtle.pendown()
    turtle.goto(x, y)
    if y<0:
        Vy = -Vy
turtle.penup()


for VoVa in range(100):
    turtle.penup()
    turtle.goto(100, 100)
    turtle.goto(-100, 100)
