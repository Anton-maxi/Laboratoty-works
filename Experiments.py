import json
students = [{"Name"        : "Vasiliy",
             "Surname"     : "Logvinov",
             "Patronymic"  : "Antonovich",
             "Adress"      : "Mira 5",
             "School"      : 9,
             "Class"       : 6},
            {"Name"        : "Anton",
             "Surname"     : "Lipovyi",
             "Patronymic"  : "Andreevich",
             "Adress"      : "Naberezhnaya 10",
             "School"      : 10,
             "Class"       : 10},
             {"Name"       : "Alina",
             "Surname"     : "Popovich",
             "Patronymic"  : "Viktorovna",
             "Adress"      : "Pushkina 5",
             "School"      : 10,
             "Class"       : 11}]
jsonData = json.dumps(students)
with open("data.json", "wt") as file:
    file.write(jsonData)
while True:
    print("Select an option:\n 1 - Add data\n 2 - View data\n 3 - Find students at 10th-11th grade\n 4 - Exit")
    x = input("Choose an option:\n")
    x = int(x)
    if x == 1:
        with open("data.json", "at") as file:
            students = json.loads(jsonData)
            def add_employee(data):
                print("Add: ")
                Name = input("Name:")
                Surname = input("Surname:")
                Patronymic = input("Patronymic:")
                Adress = input("Adress:")
                School = input("School:")
                Class = input("Class:")
                data.append({"Name": Name, "Surname": Surname, "Patronymic": Patronymic, "Adress": Adress, "School": School, "Class": Class})
                return data
            students = add_employee(students)
            jsonData = json.dumps(students)
            file.write(students)
    if x == 2:
        with open("data.json", "rt") as file:
            students = json.loads(jsonData)
            print(*students, sep='\n')
    if x == 3:
        with open("data.json", "rt") as file:
            students = json.loads(jsonData)
            school = int(input('Школа: '))
            result = [{key: value for key, value in student.items() if key  in ['Surname', 'Name', 'Patronymic', 'Adress', 'School', 'Class']}
                  for student in students if student['Class'] in [10, 11] and student ['School'] ==school]
            print(*result, sep='\n')
    if x == 4:
        quit(0)