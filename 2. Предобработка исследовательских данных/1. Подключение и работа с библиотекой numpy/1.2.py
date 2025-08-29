import numpy as np

a = np.array([1.2, 2.4, 3.6, 3.5, 6.7, 1.5, 8.4, 3.1, 9.2])

print("В массиве a ", a.size, ' строк и ', a[0].size, 'столбцов\n')

a = a.reshape((9, 1))
print(a)

a = a.reshape(3, 3)
print(a)

maxim = [0]*3
for i in range (0, 2):
    for j in range (1, 2):
        if a[i][j] > a[i][j-1]:
            maxim[i] = a[i][j]
        else:
            maxim[i] = a[i][j-1]

            
print("Максимальный элемент массива 3х3 в строках: ",maxim)

for i in range (0, 2):
    for j in range (1, 2):
        if a[i][j] > a[j][i-1]:
            maxim[1] = a[j][i]
        else:
            maxim[1] = a[j][i-1]
            
print("Максимальный элемент массива 3х3 в столбцах: ",maxim, '\n')


for i in range (0, 2):
    for j in range (1, 2):
        if a[i][j] < a[i][j-1]:
            maxim[i] = a[i][j]
        else:
            maxim[i] = a[i][j-1]

            
print("Минимальный элемент массива 3х3 в строках: ",maxim)

for i in range (0, 2):
    for j in range (1, 2):
        if a[i][j] < a[j][i-1]:
            maxim[1] = a[j][i]
        else:
            maxim[1] = a[j][i-1]
            
print("Минимальный элемент массива 3х3 в столбцах: ",maxim, '\n')


summ = 0

for i in range (0, 2):
    for j in range (0, 2):
        summ += a[i][j]

    print('Сумма элемнтов ', i, ' строки:', summ)

summ = 0

for i in range (0, 2):
    for j in range (0, 2):
        summ += a[j][i]

    print('Сумма элемнтов ', i, ' столбца:', summ)


