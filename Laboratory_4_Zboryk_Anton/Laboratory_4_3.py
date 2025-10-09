#Реалізувати функцію, яка виконує операції над списками – задану за варіантом та друк списку на екран.
#Список користувач має вводити з клавіатури.
#9. Розбиття списку на два списки за вказаним значенням інформаційного атрибуту елемента для розбиття.
def split():
    while True:
        try:
            a = list(map(int, input('Введіть масив чисел (через пробіл): ').split()))
            break
        except ValueError:
            print("Помилка: потрібно вводити лише цілі числа!")

    while True:
        try:
            filtr = int(input('Введіть число по якому буде розбиватись цей масив: '))
            if filtr not in a:
                print("Вказаного числа немає у списку!")
                continue
            break
        except ValueError:
            print("Помилка: потрібно ввести ціле число!")




    index = a.index(filtr)
    result1 = a[:index]
    result2 = a[index:]

    print("Результат розбиття:")
    print(f"Перший список (до {filtr}): {result1}")
    print(f"Другий список (з {filtr} і далі): {result2}")

split()