#Реалізувати функцію, яка виконує операції над списками – задану за варіантом та друк списку на екран.
#9. Пошук слова у списку.


def find_word ():
    a=[]
    words = [
        "яблуко",
        "груша",
        "банан",
        "Апельсин",
        "яблуко",  # повтор
        "melon",
        "watermelon",
        "слива",
        "Cherry",
        "вишня",
        "ананас",
        "grape",
        "Груша"  # та ж сама груша, але з великої
    ]
    checking=int(input("Введіть 1 якщо хочете використати список, який є за замовчуванням. 0 якщо хочете ввести свій: "))
    if checking == 1:
        a = words.copy()
        print("Список який ви будете використовувати:", *a, sep="\n")
    elif checking == 0:
        a = input('Введіть список слів (через пробіл): ').split()
        while not all(symbols_checking.isalpha() for symbols_checking in a):
            print("Помилка: потрібно вводити лише слова!")
            a = input('Введіть список слів (через пробіл): ').split()



    filtr = str(input('Введіть шукане слово: '))
    while filtr not in a:
        print("Вказаного слова немає у списку!")
        filtr = str(input('Введіть шукане слово: '))



    index=[]
    i=0
    while i<len(a):
        if a[i]==filtr:
            index.append(i)
            i+=1
        else:
            i+=1

    count_words= a.count(filtr)

    print(f"Слово знайдено!\nДовжина:{len(filtr)}\nКількість знайдених слів: {count_words}")
    print("Індекс\індекси:", *index)

find_word()