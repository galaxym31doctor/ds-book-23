def factorial(number):
    """Возвращает значение факториала числа"""
    if number == 0:
        return 1
    return number * factorial(number - 1)

def factorial_test():
    """Производит тестирование функции factiroal для первых шести
       известных значений факториалов"""

    print("Test 1 --- Ok!" if factorial(1) == 1 else "Test 1 --- Fail!")
    print("Test 2 --- Ok!" if factorial(2) == 2 else "Test 2 --- Fail!")
    print("Test 3 --- Ok!" if factorial(3) == 6 else "Test 3 --- Fail!")
    print("Test 4 --- Ok!" if factorial(4) == 24 else "Test 4 --- Fail!")
    print("Test 5 --- Ok!" if factorial(5) == 120 else "Test 5 --- Fail!")
    print("Test 6 --- Ok!" if factorial(6) == 720 else "Test 6 --- Fail!")

factorial_test()
