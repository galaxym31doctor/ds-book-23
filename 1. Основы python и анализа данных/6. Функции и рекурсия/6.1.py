def summ (a, b):
    """Возвращает сумму аргументов"""
    return (a + b)

def razn (a, b):
    """Возвращает разность аргументов"""
    return a - b

def proizv (a, b):
    """Возвращает произведение аргументов"""
    return a * b

def delen (a, b):
    """возвращает отношение первого аргумента ко второму"""
    return a / b

a = float(input())
b = float(input())

print(summ(a, b), ' ', razn(a, b), ' ', proizv(a, b), ' ', delen(a, b))


