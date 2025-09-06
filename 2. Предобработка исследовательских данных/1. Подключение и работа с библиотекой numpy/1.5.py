import numpy as np

a = np.array([[2, 8],
              [1, -6]])

b = np.array([[3, 2, 7],
              [4, 1, 8],
              [6, 3, 7]])

c = np.array([[4, 3, 2, 7],
              [6, 1, 1, -2],
              [7, 5, 8, 1],
              [9, 5, -3, -5]])

print('Транспонированная матрица а: ', a.reshape(2, 2))
print('Транспонированная матрица b: ', b.reshape(3, 3))
print('Транспонированная матрица c: ', c.reshape(4, 4), '\n')

a = np.linalg.inv(a)
print('Обратная матрица а: ', a)
b = np.linalg.inv(b)
print('Обратная матрица b: ', b)
c = np.linalg.inv(c)
print('Обратная матрица c: ', c, '\n')

print('Определитель матрицы a: ', np.linalg.det(a))
print('Определитель матрицы b: ', np.linalg.det(b))
print('Определитель матрицы c: ', np.linalg.det(c), '\n')

for i in range (0, 3):
    a1 = np.linalg.norm(b[i][0:2])
    print("Норма веркторов 2-й матрицы", i + 1, "-я строка: ", a1)

print("\n")

for i in range (0, 4):
    c1 = np.linalg.norm(c[i][0:3])
    print("Норма веркторов 3-й матрицы", i + 1, "-я строка: ", c1)

