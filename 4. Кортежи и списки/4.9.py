import random as rn

ryad = [0] * 30

for i in range (0, 30):
    ryad[i] = rn.random()

print("Неотсортированный список: ", ryad)

# С помощью сортировки вставками:
N = len(ryad)
for top in range (1, N):
    k = top
    while k > 0 and ryad[k-1] < ryad[k]:
        ryad[k], ryad[k-1] = ryad[k-1], ryad[k]
        k -= 1
        
print("Отсортированный список: ", ryad)
print("Максимальное значение: ", ryad[0])
