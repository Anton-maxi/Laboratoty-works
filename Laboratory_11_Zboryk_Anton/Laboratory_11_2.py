#Створіть датафрейм з даними використання велодоріжок за рік, заданий варіантом.
#Завантажте дані у DataFrame
#Перевірте основні характеристики датафрейму
#Визначте загальну кількість велосипедистів за рік на усіх велодоріжках
# Визначте загальну кількість велосипедистів за рік на кожній велодоріжці.
# Визначте, який місяць найбільш популярний у велосипедистів, на кожній з трьох з обраних велодоріжок.
# Побудуйте графік завантаженості однієї з велодоріжок по місяцям.

import pandas as pd
import matplotlib.pyplot as plt

# Параметри відображення
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.options.display.expand_frame_repr = False

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 5)

# Завантаження даних
df = pd.read_csv(
    'comptagevelo2010.csv',
    sep=',',
    parse_dates=['Date'],
    dayfirst=True,
    index_col='Date'
)

df.plot(figsize=(15, 10))
plt.show()

print(df.head())

print(df.info())

analysing=df.describe()

# Перейменування рядків індексу
analysing = analysing.rename(index={
    "count": "Кількість",
    "mean": "Середнє",
    "std": "Відхилення",
    "min": "Мінімум",
    "25%": "25-й перцентиль",
    "50%": "Медіана",
    "75%": "75-й перцентиль",
    "max": "Максимум"
})
print(analysing)

# 3) Додати місяць для групування
df['Month'] = df.index.month
print(df)


df_no_month = df.drop(columns=['Month'])
df_numbers = df_no_month.select_dtypes(include='number')
df_numbers_list = df_numbers.columns.tolist()

# 1.Загальна кількість велосипедистів за рік на усіх доріжках
total_coloms = df[df_numbers_list].sum()
total_all=total_coloms.sum()
print("Загальна кількість велосипедистів за рік (усі доріжки):", int(total_all))

# 2. Загальна кількість велосипедистів за рік на кожній доріжці
print("\nЗагальна кількість велосипедистів за рік на кожній доріжці:")
print(total_coloms.astype(int))

# 3. Вибір користувачем доріжок з перевірками
print("\nДоступні доріжки для вибору:")
print(", ".join(df_numbers_list))


selected_paths = []
needed = 3
while len(selected_paths) < needed:
    choice = input(f"Введіть назву доріжки №{len(selected_paths)+1}: ").strip()
    if choice == "":
        print("Порожній ввід. Введіть назву зі списку.")
        continue
    if choice not in df_numbers_list:
        hints = [c for c in df_numbers_list if choice.lower() in c.lower()]
        if hints:
            print(f"Такої доріжки немає. Можливо, ви мали на увазі: {', '.join(hints)}")
        else:
            print("Такої доріжки немає. Перевірте написання та виберіть зі списку.")
        continue
    if choice in selected_paths:
        print("Ви вже обрали цю доріжку. Виберіть іншу.")
        continue
    selected_paths.append(choice)

print("\nВи обрали доріжки:", ", ".join(selected_paths))

#4. Найпопулярніший місяць для кожної з обраних доріжок
print("\nНайпопулярніший місяць для кожної з обраних доріжок:")
month_names = {1:"Січень",2:"Лютий",3:"Березень",4:"Квітень",5:"Травень",6:"Червень",
               7:"Липень",8:"Серпень",9:"Вересень",10:"Жовтень",11:"Листопад",12:"Грудень"}

for path in selected_paths:
    monthly_sum = df.groupby('Month')[path].sum()
    best_month = int(monthly_sum.idxmax())
    best_value = int(monthly_sum.max())
    print(f"{path}: {month_names[best_month]} (кількість = {best_value})")

#5. Графік завантаженості першої обраної доріжки по місяцях

while True:
    chosen_path = input("\nВиберіть одну з обраних доріжок для побудови графіка: ").strip()
    if chosen_path not in selected_paths:
        print("Ви можете обрати лише з тих доріжок, які вже вибрали:", ", ".join(selected_paths))
    else:
        break

# Побудова графіка
monthly_counts = df.groupby('Month')[chosen_path].sum()

plt.figure(figsize=(12, 6))
monthly_counts.plot(kind='bar', color='skyblue')
plt.title(f"Завантаженість велодоріжки {chosen_path} по місяцях (2010)")
plt.xlabel("Місяць")
plt.ylabel("Кількість велосипедистів")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()



