# Write a python code that will add list of numbers together
list1=[1,2,4,6,7,9,10,11,14]
x=0
threshold=41
collate=[]
for a in list1:
    x=x+a
    if x>=threshold:
    #print(x)
        collate.append(x)
        print(collate)
