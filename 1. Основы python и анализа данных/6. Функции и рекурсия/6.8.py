import random as rn

mylist = [0] * 10

for i in range (0, 9):
    mylist[i] = rn.randint(0, 10)

newlist = list(filter(lambda x: x < 3, mylist))

print(mylist)
print(newlist)
    
