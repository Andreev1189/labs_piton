import turtle
from random import *
from random import randint
from math import cos

print('A' + 'BOBA')

# 2.0
index = [9, 1, 3, 5, 2, 6, 3, 7, 8, 0]
koord = [
[(0, 0), (0, 2), (1, 2), (1, 0), (0, 0)],
[(0, 1), (1, 2), (1, 0)],
[(0, 2), (1, 2), (1, 1), (0, 1), (0, 0), (1, 0)],
[(0, 2), (1, 2), (1, 1), (0, 1), (1, 1),  (1, 0), (0, 0)],
[(0, 2), (0, 1), (1, 1), (1, 2), (1, 0)],
[(1, 2), (0, 2), (0, 1), (1, 1), (1, 0), (0, 0)],
[(1, 2), (0, 2), (0, 1), (1, 1), (1, 0), (0, 0), [0, 1]],
[(0, 2), (1, 2), (0, 1), [0, 0]],
[(0, 2), (1, 2), (1, 1), (0, 1), (1, 1),  (1, 0), (0, 0), (0, 2)],
[(0, 1), (0, 2), (1, 2), (1, 1), (0, 1), (1, 1), (1, 0), (0, 0)]
 ]
def pic(num):
    kord = koord[index[num]]
    turtle.penup()
    for VoVa in kord:
        turtle.goto(40*VoVa[0] + num*50, 40*VoVa[1])
        turtle.pendown()
    turtle.penup()
for num in range(len(index)):
    pic(num)



for VoVa in range(100):
    turtle.penup()
    turtle.goto(100, 100)
    turtle.goto(-100, 100)
