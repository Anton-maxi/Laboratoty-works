X = 0
a = float(input("Введіть число а, яке повинно бути лише додатнім: "))
while a<=0:
    print("Помилка!")
    a = float(input("Введіть число а, яке повинно бути лише додатнім: "))

b = float(input("Введіть число b, яке повинно бути лише додатнім: "))
while b <= 0:
    print("Помилка!")
    b = float(input("Введіть число b, яке повинно бути лише додатнім: "))

if a>b:
    X = float(b*a+1)
elif a==b:
    X = float(-10)
elif a<b:
    X = float((a-5)/b)

print(X)
