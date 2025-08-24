nSet_1 = set([2, 3, 3, 3, 4, 4, 6, 7, 7, 5])
nSet_2 = set([3, 9, 8, 8, 5, 3, 4, 7, 1, 2])
maxim = [0] * 2
minim = [10] * 2


for elem in nSet_1:
    if elem >= maxim[0]:
        maxim[0] = elem
    if elem < minim[0]:
        minim[0] = elem



for elem in nSet_2:
    if elem >= maxim[1]:
        maxim[1] = elem
    if elem < minim[1]:
        minim[1] = elem


print("максимальный элемент первого множества: ", maxim[0])
print("минимальный элемент первого множества: ", minim[0])
print("максимальный элемент второго множества: ", maxim[1])
print("минимальный элемент второго множества: ", minim[1])

