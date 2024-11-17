print("Another task on list")
#task 4 - a python code to determine duplicate
duplicatebasket=[]
emptybasket=[]
listoffruits=["banana" , "watermelon" , "carrot" , "pawpaw" , "orange", "banana"]
for f in listoffruits:
    #print(f)
    emptybasket.append(f)
    if emptybasket.count(f)>1:
        duplicatebasket.append(f)
        print(duplicatebasket)