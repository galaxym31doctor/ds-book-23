staff = [['Иванов Александр', 'слесарь', 16000, 20],
['Петров Евгений', 'наладчик', 17000, 22],
['Сидоров Владимир', 'механик', 18000, 24]]

summ = 0
for i in range (0, len(staff)):
    summ += staff[i][3]

medium = summ / len(staff)

day_payment = [0] * len(staff)
for i in range (0, len(staff)):
    day_payment[i] = round(staff[i][2] / staff[i][3], 3)
    staff[i].append(day_payment[i])

N = len(staff)
for top in range (1, N):
    k = top
    while k > 0 and staff[k-1][2] < staff[k][2]:
        staff[k][2], staff[k-1][2] = staff[k-1][2], staff[k][2]
        k -= 1

print('Сотрудник | Специальность | Заработок | Дней | руб./день |')
print('--------------------------------------------------------------------')
for row in staff[:]:
    print('{: <18} | {: <14} | {: ^9.2f} | {: ^4} | {: >9.1f} |'.format(
        row[0], row[1], row[2], row[3], row[4]))
