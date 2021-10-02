#Matea Milloshi
#CS 100 2021F Section 105
#HW3, September 27,2021

#1
import turtle
import math
s = turtle.Screen()
w = turtle.Turtle()
#drawing the triangle
w.forward(100)
w.left(120)
w.forward(100)
w.left(120)
w.forward(100)

#drawing the square
w.right(60)
w.pu()
w.goto(-200,0)
w.pd()
w.forward(100)
w.right(90)
w.forward(100)
w.right(90)
w.forward(100)
w.right(90)
w.forward(100)
w.left(90)
w.pu()
w.goto(300,0)
w.pd()

#drawing the pentagon
angle=360/5
w.forward(100)
w.left(angle)
w.forward(100)
w.left(angle)
w.forward(100)
w.left(angle)
w.forward(100)
w.left(angle)
w.forward(100)
w.pu()
w.clear()
w.pd()

#2
w.pu()
w.goto(0,0)
w.pd()
radi=50
for i in range(4):
    w.down()
    w.circle(radi)
    w.up()
    w.right(90)
    w.forward(50)
    w.left(90)
    radi+=50

#3
#a
print(math.factorial(100))
#b
print(math.log2(1000000))
#c
print(math.gcd(63,49))
