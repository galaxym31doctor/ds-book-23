import numpy as np
import math

a = np.array([[2.3, 5.1, 4.7], 
              [3.5, 6.7, 1.5],
              [8.4, 3.1, 9.2]])

b = np.array([[4.3, 8.1, 6.1],
             [3.7, 1.2, 6.5],
             [2.4, 5.7, 4.7]])
size_a = a.shape
size_b = b.shape
print("Массив a содержит ", size_a[0],  " строк и ", size_a[1], " столбцов")
print("Массив b содержит ", size_b[0],  " строк и ", size_b[1], " столбцов\n")

print("Сумма: ", a + b)
print("Разность: ", a - b)
print("Произведение: ", a * b)
print("Отношение: ", a / b, '\n')

print("a^2: ", a**2, '\n')
print("b%2: ", b%2, '\n')

for i in range(0, 2):
    for j in range(0, 2):
        a[i][j] = math.cos(a[i][j])
        b[i][j] = math.sin(b[i][j])

print("cos(a) + sin(b)", a + b)