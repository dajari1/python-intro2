#write a python code that will calculate the area of a rectangle of length 10meter and breadth 8meter

l=10
b=8
Area=l*b
print(Area)

#calculate a perimeter of a rectangle
perimeter=(l+b)*2
print(perimeter)

d=Area-perimeter
print(d)

import math
radius=5
Area=math.pi*radius**2
print(Area)

#write a python code that will calculate the area of a circle radius 10 math.pi 2
math.pi=2
radius=10
Area=math.pi * radius**2
print(Area)

#Mr Jide got a loan of 450000 as principal at 5% rate for periods of 2 years. 
#Write a python code that calculate and print out the simple interest on the loan
p=450000
r=5
y=2
si=(p*r*y)/100
print("this is the simple interest",si)

#Mrs Kosovo monthly budget is #200,000 from her husband.
#She bought foodstuff for 45000
#She paid her monthly rent son her shop 10000
#She paid for children lessons 25000
#She paid her house help 10000
#Write python code that will calculate how much she has left from her budget and print it out

budget=200000
f=45000
r=10000
l=25000
h=10000
expenses=f+r+l+h
bal=budget-expenses
print(bal)