import turtle
from random import *
from random import randint
from math import cos

print('A' + 'BOBA')

# 1 6poyH
# for VoVa in range(100):
#     a = random()
#     b = random()
#     turtle.pendown()
#     turtle.forward(30*a)
#     turtle.left(360*b)
#     turtle.penup()

# 2.0
# index = [9, 1, 3, 5, 2, 6, 3, 7, 8, 0]
# koord = [
# [(0, 0), (0, 2), (1, 2), (1, 0), (0, 0)],
# [(0, 1), (1, 2), (1, 0)],
# [(0, 2), (1, 2), (1, 1), (0, 1), (0, 0), (1, 0)],
# [(0, 2), (1, 2), (1, 1), (0, 1), (1, 1),  (1, 0), (0, 0)],
# [(0, 2), (0, 1), (1, 1), (1, 2), (1, 0)],
# [(1, 2), (0, 2), (0, 1), (1, 1), (1, 0), (0, 0)],
# [(1, 2), (0, 2), (0, 1), (1, 1), (1, 0), (0, 0), [0, 1]],
# [(0, 2), (1, 2), (0, 1), [0, 0]],
# [(0, 2), (1, 2), (1, 1), (0, 1), (1, 1),  (1, 0), (0, 0), (0, 2)],
# [(0, 1), (0, 2), (1, 2), (1, 1), (0, 1), (1, 1), (1, 0), (0, 0)]
# ]
# def pic(num):
#     kord = koord[index[num]]
#     turtle.penup()
#     for VoVa in kord:
#         turtle.goto(40*VoVa[0] + num*50, 40*VoVa[1])
#         turtle.pendown()
#     turtle.penup()
#
# for num in range(len(index)):
#     pic(num)



# 4 napa6oJIa

# turtle.penup()
# x = 0
# y = 0
# Vx = 10
# Vy = 50
# ay = -10
# dt = 1
# for VoVa in range(1000):
#     x += Vx * dt
#     y += Vy * dt + ay * dt ** 2 / 2
#     Vy += ay * dt
#     turtle.pendown()
#     turtle.goto(x, y)
#     if y<0:
#         Vy = -Vy
# turtle.penup()

# 5 udeaJIbHblu ra3

# turtle.penup()
# turtle.goto(500, 500)
# turtle.pendown()
# turtle.goto(-500, 500)
# turtle.goto(-500, -500)
# turtle.goto(500, -500)
# turtle.goto(500, 500)
# turtle.penup()
#
# pool = [turtle.Turtle(shape='circle') for i in range(7)]
# pol = []
# for unit in pool:
#     a = randint(0, 360)
#     pol.append(a)
#     unit.penup()
#     unit.speed(11)
#     unit.goto(randint(-500, 500), randint(-500, 500))
#     unit.left(a)
#
# print(pol)
# for i in range(1000):
#     for unit in pool:
#         num = pool.index(unit)
#         if unit.xcor() > 500:
#             unit.right(2*pol[num]+180)
#             pol[num] = 180-pol[num]
#         if unit.xcor() < -500:
#             unit.right(2*pol[num]+180)
#             pol[num] = 180-pol[num]
#         if unit.ycor() > 500:
#             unit.right(2*pol[num])
#             pol[num] = -pol[num]
#         if unit.ycor() < -500:
#             unit.right(2*pol[num])
#             pol[num] = -pol[num]
#         unit.forward(10)







# B_Mupe_ecTb_2_Tuna_JII0geu_-_nepBble_geJIaI0T_BblBogbl_Ha_ocHoBe_HenoJIHblx_gaHHblx























for VoVa in range(100):
    turtle.penup()
    turtle.goto(100, 100)
    turtle.goto(-100, 100)
