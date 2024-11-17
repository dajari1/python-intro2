# Write a python code that will add list of numbers together
list1=[1,2,4,6,7,9,10]
x=0
threshold=13
collate=[]
for a in list1:
    x=x+a
    if x<=threshold:
    #print(x)
        collate.append(x)
        print(collate)