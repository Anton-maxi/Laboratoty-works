import math

def calcul_z (a):
    funk = math.exp(a)+math.sqrt(a)
    return funk
def sum_of_number (b):
    # Запитуємо число у користувача
    # Робимо число додатним, щоб працювало і з від'ємними
    num = abs(b)

    sum_digits = 0

    # Поступово відокремлюємо останню цифру і додаємо її до суми
    while num > 0:
        sum_digits += num % 10  # додаємо останню цифру
        num //= 10  # відкидаємо останню цифру
    return sum_digits


print("Функція: e^x+sqrt(x)")
x=float(input("Введіть х: "))
while x<0:
    print("Помилка! х має бути НЕ менше нуля")
    x = float(input("Введіть х: "))
z= calcul_z(x)
print("z=", z)
n= float(input("Введіть число, щоб порахувати суми його цифр: "))
sum_n= sum_of_number(n)
print("Сума цифр =", sum_n)
