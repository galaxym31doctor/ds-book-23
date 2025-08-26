fruits = ("яблоко", "банан", "апельсин", "груша", "мандарин")
mass = (5, 8, 3, 5, 10)

x = input()

for i in range(1, 5):
    if x == fruits[i]:
        print(mass[i])
        break
