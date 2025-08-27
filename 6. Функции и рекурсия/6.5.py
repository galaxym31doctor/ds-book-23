def factorial(number):
    """Возвращает значение факториала числа"""
    if number == 0:
        return 1
    return number * factorial(number - 1)

chislo = int(input())

print(factorial(chislo))
