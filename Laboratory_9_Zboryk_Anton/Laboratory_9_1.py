#Напишіть програму для обробки .csv файла та збереження результатів у інший .csv файл. У програмі реалізувати обробку помилок відкриття файлу за допомогою конструкції try-except.
#Варіант 9. Знайти дані Population, total для України за 1991-2019 роки. Вивести вміст .csv файлу на екран.
#Організувати пошук найнижчого та найвищого значень показника та записати результат пошуку у новий .csv файл.
import csv


try:

    csvfile = open("Population.csv","r")

    reader = csv.DictReader(csvfile, delimiter = ",")
    print("Україна 1991-2019")
    print("Рік     Значення")

    for row in reader:

        print(row['Time'], ': ', row["Value"])

    csvfile.close()

except IOError:

    print("Файл Population.csv не знайдено!")

try:

    csvfile = open("Population.csv","r")

    reader = csv.DictReader(csvfile, delimiter = ",")

    for row in reader:
        start = [int(row['Time']), int(row['Value'])]
        min_value = [int(row['Time']), int(row['Value'])]
        max_value = [int(row['Time']), int(row['Value'])]
        break

    for row in reader:
        now = [int(row['Time']), int(row['Value'])]

        if start[1] > now[1]:
            start[0] = now[0]
            start[1] = now[1]
            min_value[0]=now[0]
            min_value[1]=now[1]
        if start[1] < now[1]:
            start[0] = now[0]
            start[1] = now[1]
            max_value[0]=now[0]
            max_value[1]=now[1]
    print(f"Максимум населення було в: {max_value[0]} році, і воно становило:{max_value[1]} чоловік")
    print(f"Мінімум населення було в: {min_value[0]} році, і воно становило:{min_value[1]} чоловік")

    csvfile.close()


except IOError:

    print("Файл Population.csv не знайдено!")