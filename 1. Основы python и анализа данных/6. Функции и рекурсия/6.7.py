import random as rn

mylist = [0] * 10

for i in range (0, 9):
    mylist[i] = rn.randint(0, 100)

newlist = list(map(lambda x: x**2, mylist))

print(mylist)
print(newlist)
    
