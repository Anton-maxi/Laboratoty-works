import matplotlib.pyplot as plt
#Скоригований чистий національний дохід на душу населення (у поточних доларах США)

import csv


try:

    with open("Adjusted net national income per capita.csv", "r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        y_ukraine = []
        y_poland=[]
        x=[]
        for field in reader.fieldnames:
            if "YR" in field:
                # беремо тільки число до пробілу (2000, 2001, ...)
                x.append(int(field.split()[0]))

        for row in reader:
            if row["Country Name"] == "Ukraine":
                # пройтися по всіх стовпчиках з роками
                for year in row.keys():
                    if "YR" in year:  # відфільтруємо тільки рік
                        value = row[year]
                        if value:  # перевірка, що не пусто
                            y_ukraine.append(float(value))
            if row["Country Name"] == "Poland":
                # пройтися по всіх стовпчиках з роками
                for year in row.keys():
                    if "YR" in year:  # відфільтруємо тільки рік
                        value = row[year]
                        if value:  # перевірка, що не пусто
                            y_poland.append(float(value))



except IOError:

    print("Файл Adjusted net national income per capita.csv не знайдено!")


plt.plot(x, y_ukraine, label='Ukraine', color= 'y',linewidth = 5)
plt.plot(x, y_poland, label='Poland', color= 'b',linewidth = 5)
plt.title('Завдання 2', fontsize=15)
plt.xlabel('Year', fontsize=12, color='r') # позначення вісі абсцис
plt.ylabel('$ USA', fontsize=12, color='r') # позначення вісі ординат
plt.legend()
plt.grid()
plt.xticks(x[::5])
plt.show()

flag=False

while flag==False:
    choice = input("Оберіть для якої країни вивести стовпчикову діаграму!\nВпишіть або назву 'Ukraine' або 'Poland', щоб вивести стовпчикову діаграму для цієї країни\n")
    if choice.lower() == "ukraine":
        y = y_ukraine
        flag=True
    elif choice.lower() == "Poland":
        y = y_poland
        flag = True
    else:
        print("Помилка! Введіть назву країни ще раз!")

ax = plt.gca()
ax.bar(x, y)

ax.set_xticks(x)

ax.set_xticklabels([str(year) for year in x], rotation=45)

plt.show()



