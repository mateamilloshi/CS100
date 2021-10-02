#Matea Milloshi
#CS 100 2021F Section 105
#HW04, September 28,2021

import math
#1a
a=3
b=4
c=5

#b
if a < b :
  print('OK')

#c
if c<b:
  print('OK')

#d
if a+b==c:
  print('OK')

#e
if (a**2)+(b**2)==(c**2):
  print('OK')

#2

if a < b :
    print('OK')
else:
    print('NOT OK')

if c<b:
    print('OK')
else:
    print('NOT OK')

if a+b==c:
    print('OK')
else:
    print('NOT OK')

if (a**2)+(b**2)==(c**2):
    print('OK')
else:
    print('NOT OK')

#3
import turtle

input_color = input('What color?')
input_width = int(input('What line width?'))
length = int(input('What line length?'))
shape = input('Line, triangle or square?')

s = turtle.Screen()
t=turtle.Turtle()

t.color(input_color)
t.width(input_width)

if shape=='line':
    t.forward(length)

elif shape=='triangle':
    t.down()
    t.forward(length)
    t.left(120)
    t.forward(length)
    t.left(120)
    t.forward(length)
    t.left(120)

elif shape=='square':
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)


