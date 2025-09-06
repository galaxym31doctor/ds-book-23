import numpy as np
import random

a = np.array([random.randint(0, 100) for i in range(0, 100, 1)])

#Первое решение задачи: с использованием цикла for
count = 0
for i in range (0, 100):
    if(a[i] > 50):
        count += 1
        
print(count)

count = 0
count = (a > 50).sum()

print(count)