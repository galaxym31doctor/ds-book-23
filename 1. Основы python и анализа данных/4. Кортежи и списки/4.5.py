import random

n = int(input())
A = [0] * n
summ=0
for i in range(1, n):
    A[i] = random.random()
    summ += A[i]

print(summ)




