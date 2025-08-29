n = int(input())
k = int(input())

A = range(n, k)

total_even = 0
total_odd = 0

for i in range(0, k-1, 2):
    total_even += A[i]
for i in range(1, k-1, 2):
    total_odd += A[i]

print("Сумма четных элементов больше" if total_even > total_odd else "Сумма нечетных элементов больше")

for i in range(0, k-1):
    if A[i]%2 == 0:
        total_even += A[i]
    else:
        total_odd += A[i]
print("Сумма четных элементов больше" if total_even > total_odd else "Сумма нечетных элементов больше")1


