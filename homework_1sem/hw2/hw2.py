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

# 3
# MGY(4, 30, 0, 0)

# 4
# w(10, 0, 0)

# 5
# for i in range (30):
# 	MGY(4, 10*(i+1), 0, 0)

# 6
# n = 12
# for VoVa in range(n):
# 	turtle.left(360 / n)
# 	turtle.forward(80)
# 	turtle.stamp()
# 	turtle.goto(0, 0)

# 7
# for VoVa in range(360*7):
# 	turtle.forward(3*2*3.1416/360*((1+(2*3.1416/360*VoVa)**2)**(1/2)))
# 	turtle.left(1)

# 8
# for VoVa in range(30):
# 	turtle.forward(20*(VoVa+1))
# 	turtle.left(90)
# 	turtle.forward(20 * (VoVa + 1))
# 	turtle.left(90)

# 9
# for i in range(100):
# 	MGY(i+3, (i+1)*10, 0, 0)

# 10
# n = 6
# for VoVa in range(n):
# 	w(50, 50*cos(2*3.1416/n*VoVa), 50*sin(2*3.1416/n*VoVa))

# 11
# for VoVa in range(10):
# 	w(20 + 4 * VoVa, 20 + 4 * VoVa, 0)
# 	w(20 + 4 * VoVa, -20 - 4 * VoVa, 0)

# 12
def v(R):
	turtle.penup()
	turtle.pendown()
	turtle.left(2)
	for VoVa in range(45):
		turtle.forward(2*3.1416*R/90)
		turtle.left(4)
	turtle.right(2)
	turtle.penup()

# for VoVa in range(10):
# 	v(50)
# 	v(10)

# 13
# turtle.color('red')
# turtle.begin_fill()
# w(50, 0, 0)
# turtle.end_fill()
# turtle.color('black')
# turtle.begin_fill()
# w(7, 25, 15)
# turtle.end_fill()
# turtle.begin_fill()
# w(7, -25, 15)
# turtle.end_fill()
#
# turtle.color('green')
# turtle.goto(-25, -10)
# turtle.right(90)
# turtle.width(2)
# v(25)
#
# turtle.goto(0, 0)
# turtle.stamp()
# for VoVa in range(1):
# 	turtle.goto(100, 100)
# 	turtle.goto(-100, 100)

# 14
# star(5, 30)
# star(11, 30)