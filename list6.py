#task 5 - summation of list of numbers
total=0
listofnumbers=[400, 200, 50, 10, 19, 150, 0, 5]
for i in listofnumbers:
    total=total+i
print(total)
#task 6 - multiplication of the above numbers
multiply=1
listofnumbers2=[40, 20, 5, 10, 9, 15]
for i in listofnumbers2:
    multiply=multiply*i
print(multiply)
#division of the above result
result=multiply/1000
print(result)
if result>100:
    print("Hurray the result is greater than 100")
    output=(result/10)+5
    print(output)
else:
    output1=result+500
    print(output1)