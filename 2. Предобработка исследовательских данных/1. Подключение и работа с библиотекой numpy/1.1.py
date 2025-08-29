import numpy as np
import math

a = np.array([[2.3, 5.1, 4.7],
[3.5, 6.7, 1.5],
[8.4, 3.1, 9.2]])

b = np.array([[4.3, 8.1, 6.1],
[3.7, 6.2, 1.5],
[2.4, 5.7, 4.7]])

print("В массиве a ", a.size, ' строк и ', a[0].size, 'столбцов')
print("В массиве b ", b.size, ' строк и ', b[0].size, 'столбцов\n')

print("Сумма массивов: a + b = ", a + b)
print("Разность массивов: a - b = ", a - b)
print("Произведение массивов: a * b = ", a * b)
print("частное массивов: a / b = ", a / b, "\n")

c = a ** 2
print("Массив a в квадрате:", с, "\n")

c_cos = math.cos(a)
s_Sin = math.sin(a)

print("косинус первого массива + синус второго:", c_cos + s_sin)

