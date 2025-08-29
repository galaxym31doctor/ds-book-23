import random as rn
import math
ryad = [0] * 10

arifm = 0
dispertion = 0
quard = 0

for i in range (0, 10):
    ryad[i] = rn.random()
    arifm += ryad[i]

arifm /= 10

for i in range(0, 10):
    dispertion += (ryad[i] - arifm) ** 2

dispertion /= 10
quard = math.sqrt(dispertion)


print("Полученный ряд случайных чисел: ", ryad)
print("Среднее арифметическое: ", arifm)
print("Дисперсия: ", dispertion)
print("Среднее квадратическое:", quard)
