import matplotlib.pyplot as plt
import numpy as np

# Вхідні дані
name = ['Андрій Коваленко Сергійович', 'Марія Шевченко Олександрівна',
        'Олег Бондаренко Ігорович','Ірина Мельник Василівна',
        'Дмитро Савченко Петрович','Оксана Лисенко Андріївна',
        'Володимир Гриценко Михайлович','Наталія Романюк Степанівна',
        'Тарас Дорошенко Юрійович','Катерина Сидоренко Вікторівна']

height = [172, 165, 178, 160, 181, 168, 185, 162, 176, 170]
sex = ['чоловік', 'жінка', 'чоловік', 'жінка', 'чоловік', 'жінка',
       'чоловік', 'жінка', 'чоловік', 'жінка']

students = dict(zip(name, [{"Зріст": h, "Стать": s} for h, s in zip(height, sex)]))

# Функція для підрахунку сумарного зросту
def compare_heights(database):
    girls = sum(p["Зріст"] for p in database.values() if p["Стать"] == "жінка")
    boys = sum(p["Зріст"] for p in database.values() if p["Стать"] == "чоловік")
    return girls, boys

# Отримуємо дані
girls_total, boys_total = compare_heights(students)

# Побудова кругової діаграми
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

data = [boys_total, girls_total]
labels = ["Хлопці", "Дівчата"]

def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return f"{pct:.1f}%\n({absolute} см)"

wedges, texts, autotexts = ax.pie( data, autopct=lambda pct: func(pct, data), textprops=dict(color="w"))

ax.legend(wedges, labels, title="Стать", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")
ax.set_title("Загальний зріст студентів за статтю")

plt.show()