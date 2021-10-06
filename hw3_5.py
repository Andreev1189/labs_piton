import turtle
from random import *
from random import randint
from math import cos

print('A' + 'BOBA')


# 5 udeaJIbHblu ra3

turtle.penup()
turtle.goto(500, 500)
turtle.pendown()
turtle.goto(-500, 500)
turtle.goto(-500, -500)
turtle.goto(500, -500)
turtle.goto(500, 500)
turtle.penup()
pool = [turtle.Turtle(shape='circle') for i in range(7)]
pol = []

for unit in pool:
    a = randint(0, 360)
    pol.append(a)
    unit.penup()
    unit.speed(11)
    unit.goto(randint(-500, 500), randint(-500, 500))
    unit.left(a)
    
print(pol)

for i in range(1000):
    for unit in pool:
        num = pool.index(unit)
        if unit.xcor() > 500:
            unit.right(2*pol[num]+180)
            pol[num] = 180-pol[num]
        if unit.xcor() < -500:
            unit.right(2*pol[num]+180)
            pol[num] = 180-pol[num]
        if unit.ycor() > 500:
            unit.right(2*pol[num])
            pol[num] = -pol[num]
        if unit.ycor() < -500:
            unit.right(2*pol[num])
            pol[num] = -pol[num]
        unit.forward(10)



for VoVa in range(100):
    turtle.penup()
    turtle.goto(100, 100)
    turtle.goto(-100, 100)
