import random

n = int(input())
A = [0] * n

for i in range(1, n):
    A[i] = random.random()

print(A)
print(A.sort())
print(max(A), min(A))
