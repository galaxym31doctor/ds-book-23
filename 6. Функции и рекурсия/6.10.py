def column_total(films, start_year, end_year):
    end = 0
    while end < 10:
        if films[end][1] <= end_year:
            break
        end += 1

    start = 9
    while start > 0:
        if films[start][1] >= start_year:
            break
        start -= 1

    summ = 0
    for i in range(end, start):
        summ += films[i][5]
        
    return summ

 
def column_mean(films, start_year, end_year):
    end = 0
    while end < 10:
        if films[end][1] <= end_year:
            break
        end += 1

    start = 9
    while start > 0:
        if films[start][1] >= start_year:
            break
        start -= 1

    summ = 0
    for i in range(end, start):
        summ += films[i][5]
        
    return summ / (start-end)


def middle(films):
    new_films = list(films)

    for i in range (0, 9):
        new_films[i].append(round(new_films[i][3]/new_films[i][5], 2))

    
    new_films.sort(key=lambda i: i[-1],reverse=True)
        
    return new_films
    
        



films = [
    ['Назад в будущее', 1985, 8.6, 116, ['фант.', 'комедия'], 19.0, 381.1],
    ['Назад в будущее 2', 1989, 8.3, 108, ['фант.', 'прикл.'], 40.0, 331.9],
    ['Малыш', 1921, 8.2, 68, ['драма', 'комедия'], 0.25, 5.45],
    ['Один дома', 1990, 8.2, 103, ['семейный', 'комедия'], 18.0, 476.68],
    ['Один дома 2', 1992, 7.9, 119, ['семейный', 'комедия'], 18.0, 358.9],
    ['Большой', 1988, 7.9, 104, ['фэнтези', 'мелодрама'], 18.0, 151.6],
    ['Рыжий пёс', 2011, 7.7, 92, ['мелодрама', 'комедия'], 8.5, 21.18],
    ['Марли и я', 2008, 7.8, 115, ['драма', 'комедия'], 60.0, 255.7],
    ['Миссис Даутфайр', 1993, 7.7, 125, ['драма', 'комедия'], 25.0, 441.28],
    ['Кудряшка Сью', 1991, 7.6, 101, ['семейный', 'комедия'], 25.0, 33.6]
]

films.sort(key=lambda i: i[1],reverse=True)

print('Название фильма| Год | Рейтинг | Длина | Бюджет | Сборы |')
print('--------------------------------------------------------------------')
for row in films[:]:
    print('{: <35} | {} | {: >7.2f} | {: >5} | {: >6.1f} | {: >6.1f} |'.format(
        row[0], row[1], row[2], row[3], row[5], row[6]))
    
print("\nCумма бюджетов (или сборов) всех фильмов в списке за выбранный период времени: ",
      column_total(films, 1989, 1992), "\n")
print("Cреднее значение бюджетов (или сборов) всех фильмов в списке за выбранный период времени: ",
      column_mean(films, 1989, 1992), "\n")

print('Название фильма| Год | Рейтинг | Длина | Бюджет | Сборы |Бюджет за минуту|')
print('--------------------------------------------------------------------')
for row in middle(films)[0:7]:
    print('{: <35} | {} | {: >7.2f} | {: >5} | {: >6.1f} | {: >6.1f} |{: >6.1f} |'.format(
        row[0], row[1], row[2], row[3], row[5], row[6], row[-1]))

