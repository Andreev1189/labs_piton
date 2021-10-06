import turtle
from math import cos

print('A' + 'BOBA')

def w(R, OX, OY):
	turtle.penup()
	turtle.goto(OX, OY-R)
	turtle.pendown()
	turtle.left(2)
	for VoVa in range (90):
		turtle.forward(2*3.1416*R/90)
		turtle.left(4)
	turtle.right(2)
	turtle.penup()

def MGY(N, R, OX, OY):
	turtle.penup()
	turtle.goto(OX, OY-R)
	turtle.pendown()
	turtle.left(360/N/2)
	for VoVa in range (N):
		turtle.forward(2**(1/2)*R*(1-cos(3.1416/180*360/N))**(1/2))
		turtle.left(360/N)
	turtle.right(360/N/2)
	turtle.penup()

def star(N, L):
	turtle.penup()
	turtle.goto(L/2/cos(90/N), 0)
	turtle.pendown()
	turtle.left(90/N)
	for VoVa in range(N):
		turtle.forward(L)
		turtle.right(180*(N-1)/N)
	turtle.right(90/N)
	turtle.penup()


# 14
star(5, 30)
star(11, 30)

