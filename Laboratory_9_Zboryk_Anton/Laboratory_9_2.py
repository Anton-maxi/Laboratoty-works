#відповідно до свого варіанту написати програму, яка створює об’єкт JSON для збереження даних із заданої предметної області та виконує обробку даних.
#Реалізувати у вигляді окремих функцій та організувати їх виклик користувачем у діалоговому режимі:
# виведення на екран вмісту JSON файлу;
# додавання (видалення) нового запису у JSON файл;
# пошук даних у JSON файлі за одним із полів на вибір;
# розв’язання завдань відповідно до варіанту, результат виконання завдання записати в інший JSON файл.
#Варіант 9. Задано дані про зріст n=10 учнів класу, впорядковані за зменшенням (немає жодної пари учнів, які мають однаковий зріст).
# Скласти програму, яка визначає чи перевищує сумарний зріст дівчат у класі зріст хлопців.
import json


name = ['Андрій Коваленко Сергійович', 'Марія Шевченко Олександрівна', 'Олег Бондаренко Ігорович','Ірина Мельник Василівна','Дмитро Савченко Петрович','Оксана Лисенко Андріївна','Володимир Гриценко Михайлович','Наталія Романюк Степанівна','Тарас Дорошенко Юрійович','Катерина Сидоренко Вікторівна']
height= [172, 165, 178, 160, 181, 168, 185, 162, 176, 170]
sex=['чоловік', 'жінка', 'чоловік', 'жінка', 'чоловік', 'жінка', 'чоловік', 'жінка', 'чоловік', 'жінка']

students = dict(  zip( name, [{"Зріст": h, "Стать": s} for h, s in zip(height, sex)] )  )




def print_students(database):
    for student_name, props in database.items():
        print(f"{student_name}: {props['Зріст']} см, {props['Стать']}")


def add_student(database_new):
    student_name_new = input("Введіть ПІБ студента: ")
    student_height_new = int(input("Введіть зріст студента: "))
    student_sex_new= input("Введіть стать студента:")
    if student_name_new not in database_new:
        database_new[student_name_new] = {"Зріст": student_height_new, "Стать": student_sex_new}
        print(f"Студента {student_name_new} додано до бази даних.")
        return True
    else:
        print("Такий студент є!")
        c = int(input("Хочете додати нового студента? Введіть 1, якщо так, 0 якщо ні: "))
        if c == 1:
            add_student(database_new)
        else:
            return False

def delete_student(database, student_name):
    if student_name in database:
        del database[student_name]
        print(f"Студента {student_name} видалено.")
    else:
        print("Студента не знайдено!")

def change_student_height (database, student_name):
    if student_name in database:
        new_height = int(input("Введіть новий зріст: "))
        database[student_name]["Зріст"] = new_height
        print(f"Зріст студента {student_name} змінено.")

    else:
        print("Студента не знайдено!")
        c = int(input("Хочете додати нового студента? Введіть 1, якщо так, 0 якщо ні: "))
        if c == 1:
            add_student(database)


def search_student(database):
    key = input("Введіть поле для пошуку (ПІБ/Зріст/Стать): ")
    value = input("Введіть значення для пошуку: ")
    results = []
    if key.lower() == "піб":
        if value in database:
            results.append((value, database[value]))
    elif key.lower() == "зріст":
        value = int(value)
        results = [(n, p) for n, p in database.items() if p["Зріст"] == value]
    elif key.lower() == "стать":
        results = [(n, p) for n, p in database.items() if p["Стать"] == value]
    else:
        print("Невірне поле!")
        return
    for n, p in results:
        print(f"{n}: {p['Зріст']} см, {p['Стать']}")

def compare_heights(database):
    girls = sum(p["Зріст"] for p in database.values() if p["Стать"] == "жінка")
    boys = sum(p["Зріст"] for p in database.values() if p["Стать"] == "чоловік")
    result = {"Сума дівчат": girls, "Сума хлопців": boys, "Дівчата > Хлопці": girls > boys}
    with open("Result.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=4)
    print("Результат записано у Result.json")




def save_to_file(database):
    try:
        with open("Student.json", "w+", encoding="utf-8") as file:
            json.dump(database, file, ensure_ascii=False, indent=4)

    except FileNotFoundError:
        print("Файл Student.json не знайдено!")

def load_from_file():
    try:
        with open("Student.json", "r+", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        print("Файл Student.json не знайдено!")

while True:
    students_sorted = dict(sorted(students.items(), key=lambda x: x[1]["Зріст"], reverse=True))
    save_to_file(students_sorted)
    print("\nМеню:")
    print("Вивести усіх студентів - 1")
    print("Додати нового студента - 2")
    print("Видалити студента - 3")
    print("Змінити зріст студента - 4")
    print("Пошук за властивостю (ПІБ, зріст, стать) - 5")
    print("Визначити чи перевищує сумарний зріст дівчат у класі зріст хлопців - 6")
    print("Вийти з програми - 0")
    choice = input("Введіть пункт меню: ")


    if choice == "1":
        student_json= load_from_file()
        print_students(student_json)

    elif choice == "2":
        add_student(students)


    elif choice == "3":
        del_name = input("Введіть ПІБ студента для видалення: ")
        delete_student(students, del_name)


    elif choice == "4":
        student_update=input("Введіть ПІБ студента, дані якого хочете змінити: ")
        change_student_height(students, student_update)

    elif choice == "5":
        student_json = load_from_file()
        search_student(student_json)

    elif choice == "6":
        compare_heights(students)


    elif choice == "0":
        print("Вихід із програми...")
        break

    else:
        print("Невірний вибір, спробуйте ще раз!")
