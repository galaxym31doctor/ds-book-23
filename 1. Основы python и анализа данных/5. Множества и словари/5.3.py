import random as rand

A = [0] * 10

for i in range (1, 10):
    A[i] = rand.uniform(1, 10)
    
nSet = set(A)
nSet_1 = set(A ^ 2)
print(nSet ^ 2)

