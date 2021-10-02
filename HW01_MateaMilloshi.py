
#Matea Milloshi
#CS 100 2021F Section 105
#HW01, September 12,2021
import math
age = 23
year = 2021
fall_courses = 4

lenth = 2.2
width = 4.3
depth = 6.5

month = 'september'
fav_season = 'fall'
colour = 'blue'

#Exercise 1.1 
#1. In a print statement, if you leave out one parenthesis or both
#and try to run the program, an error occurs "invalid syntax"
#2.print('hello),if we leave a out a quotation mark, an error
#occurs, "EOL while scanning string literal" and if we leave out both
#quotation marks,the following error appears "name 'helo' is not defined
#3. num=+2, this statement is legal, if you print n then
#you will have 2, the sign will not appear and the statement n=2++2, adds the number
#so if you print(n) then it will equal to 4.

#Exercise 1.2
#1
seconds = 42*60 + 42
print(seconds)  #2562
#2
miles = 10/1.61
print(miles)    #6.211180124223602
#3
seconds = 2562/(10/1.61)
print(seconds)  #412.482
minutes = 412.482/60
print(minutes)  #6.874700000000001
hours = (10/1.6)/(2562/3600)
print(hours)    #8.782201405152225

#Exercise 2.1
#42=n is not legal, error occurs "cannot assign to literal"
#x = y = 1 is legal, x, y are each assigned the value 1
#if you put a semi-colon at the end of a python statement no error occurs.
#the semi-colon allows you to write multiple statements on the same line
#If we put a period at the end of an assignment statement, no error will occur.
#ex x=1. However, in python if we we use a period at the end of any other statement
#it will result in an error.
#python interprets xy as a single variable and not as a multiplication. Therefore
#if its used it will pop up an error.To multiply two variable we have to use x*y syntax.

#Exercise 2.2
#1
a=(4/3)*math.pi*math.pow(5,3)
print(a) #523.5987755982989
#2
cost=24.96*60+3+((75*59)/100)-((0.40*24.95)*60)
print(cost) #946.0500000000001
#
mins= 8+7*3+8
secs=15+12*3+15
print(mins)
print(secs)
print('You will be home by 7:31am')


