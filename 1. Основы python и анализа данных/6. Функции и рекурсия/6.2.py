def num(number, k = 2):
    """Возводит число number в степень k, которая по умолчаниюравна 2"""
    if k == 1:
        return number
    return number * num(number, k-1)

def test_num():
    """Запускает функцию num и тестирует ее работу"""
    i = 1
    while i != 11:
        print("Test 1." + str(i) + " - Ok!" if num(2, i) == 2 ** i
              else "Test 1." + str(i) + " - Fail!")
        i += 1

    print()

    i = 1
    while i != 11:
        print("Test 2." + str(i) + " - Ok!" if num(i, 2) == i ** 2
              else "Test 2." + str(i) + " - Fail!")
        i += 1

test_num()
        
