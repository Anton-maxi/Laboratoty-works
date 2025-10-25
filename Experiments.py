#Задано дані про зріст n=10 юнаків класу, впорядковані за зменшенням (немає жодної пари учнів, які мають однаковий зріст).
#На початку навчального року до класу вступив новий учень (його зріст не співпадає із зростом жодного з учнів класу,
#перевищує зріст самого низького учня і менше зросту найвищого).
# Скласти програму, яка визначає:
# а) прізвища всіх учнів, зріст яких менше росту «новенького»;
# б) прізвище учня, після якого слід записати прізвище «новенького», щоб впорядкованість не порушилася;
# в) прізвище учня, зріст якого найменше відрізняється від росту «новенького»

name = ['Андрій Коваленко Сергійович', 'Марія Шевченко Олександрівна', 'Олег Бондаренко Ігорович','Ірина Мельник Василівна','Дмитро Савченко Петрович','Оксана Лисенко Андріївна','Володимир Гриценко Михайлович','Наталія Романюк Степанівна','Тарас Дорошенко Юрійович','Катерина Сидоренко Вікторівна']
height = [172, 165, 178, 160, 181, 168, 185, 162, 176, 170]
students=dict(zip(name, height))



def print_students(database):
    for student_name, h in database.items():
        print(f"{student_name}: {h} см")

def add_student(database_new):
    student_name_new = input("Введіть ПІБ студента: ")
    student_height_new = int(input("Введіть зріст студента: "))
    if student_name_new not in database_new:
        database_new[student_name_new] = student_height_new
        print(f"Студента {student_name_new} додано до бази даних.")
        return student_name_new, student_height_new
    else:
        print("Такий студент є!")
        c = int(input("Хочете оновити дані цього студента? Введіть 1, якщо так, 0 якщо ні: "))
        if c ==1:
            change_student_height(database_new, student_name_new)
            return None, None
        else:
            return None,None

def delete_student(database, student_name):
    if student_name in database:
        del database[student_name]
        print(f"Студента {student_name} видалено.")
    else:
        print("Студента не знайдено!")

def change_student_height (database, student_name):
    if student_name in database:
        database[student_name]=int(input("Введіть оновлений зріст: "))
    else:
        print("Студента не знайдено!")
        c = int(input("Хочете додати нового студента? Введіть 1, якщо так, 0 якщо ні: "))
        if c == 1:
            add_student(database)


def height_compare(database, student_name):
    result = []
    student_reverse= dict(sorted(database.items(),key=lambda x: x[1], reverse=False))
    if student_name in database:
        for key in student_reverse:
            if database[student_name] > student_reverse[key]:
                result.append(key)
        print(f"Студенти які мають менший зріст за {student_name}: ")
        print(*result, sep=", ")
    else:
        print("Ви не додали нового студента!")
        c = int(input("Хочете додати нового студента? Введіть 1, якщо так, 0 якщо ні: "))
        if c == 1:
            add_student(database)



def next_student(database, student_name, new_height):
    if student_name not in database:
        print("Ви не додали нового студента!")
        c = int(input("Хочете додати нового студента? Введіть 1, якщо так, 0 якщо ні: "))
        if c == 1:
            add_student(database)
        else:
            return
    # Сортуємо за спаданням
    sorted_database = sorted(database.items(), key=lambda x: x[1], reverse=True)
    for i in range(len(sorted_database)):
        name_student, h = sorted_database[i]
        # шукаємо перший зріст, який менший за новенького
        if h < new_height:
            # тоді новенького треба ставити після попереднього
            prev_name, prev_h = sorted_database[i-2]
            print(f"Новенького слід записати після: {prev_name} (його зріст {prev_h} см)")
            return
    # якщо новенький найнижчий
    print("Новенький має найменший зріст, його слід записати останнім.")

def minimal_difference(database, student_name_new, new_height):
    if student_name_new not in database:
        print("Ви не додали нового студента!")
        c = int(input("Хочете додати нового студента? Введіть 1, якщо так, 0 якщо ні: "))
        if c == 1:
            add_student(database)
        else:
            return
    database_sorted = sorted(database.items(), key=lambda x: x[1], reverse=True)
    for i in range(len(database_sorted)):
        name_student_central, h_central = database_sorted[i-1]
        if h_central == new_height:
            prev_name, prev_h = database_sorted[i-2]
            next_name, next_h = database_sorted[i]
            prev_difference = prev_h - h_central
            next_difference = h_central- next_h
            if prev_difference < next_difference:
                print(f"Студент, зріст якого найменше відрізняється від росту «новенького»: {prev_name} (різниця: {prev_difference})")
            elif prev_difference > next_difference:
                print(f"Студент, зріст якого найменше відрізняється від росту «новенького»: {next_name} (різниця: {next_difference})")
            elif prev_difference == next_difference:
                print(f"Студенти, зріст яких найменше відрізняється від росту «новенького»: {next_name} та {prev_name} (різниця: {next_difference})")
    return




new_student_name = None
new_student_height =None

while True:
    students_sorted = dict(sorted(students.items(), key=lambda x: x[1], reverse=True))
    print("\nМеню:")
    print("Вивести усіх студентів - 1")
    print("Додати нового студента - 2")
    print("Видалити студента - 3")
    print("Змінити зріст студента - 4")
    print("Вивести студентів, зріст яких менший росту «новенького» - 5")
    print("Вивести студента, після якого слід записати прізвище «новенького», без порушення порядку - 6")
    print("Вивести студента, зріст якого найменше відрізняється від росту «новенького» - 7")
    print("Вийти з програми - 0")
    choice = input("Введіть пункт меню: ")


    if choice == "1":
        print_students(students_sorted)

    elif choice == "2":
        new_student_name, new_student_height =add_student(students)


    elif choice == "3":
        del_name = input("Введіть ПІБ студента для видалення: ")
        delete_student(students, del_name)

    elif choice == "4":
        student_update=input("Введіть ПІБ студента, дані якого хочете змінити: ")
        change_student_height(students, student_update)

    elif choice == "5":
        height_compare(students, new_student_name)


    elif choice == "6":
        next_student(students, new_student_name, new_student_height)

    elif choice == "7":
        minimal_difference(students_sorted, new_student_name, new_student_height)


    elif choice == "0":
        print("Вихід із програми...")
        break

    else:
        print("Невірний вибір, спробуйте ще раз!")