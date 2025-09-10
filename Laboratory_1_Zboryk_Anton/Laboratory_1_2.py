Sum = 0
product = 1
for i in range(0,21):
    if i % 2 == 0:
        Sum += i
    else:
        product *= i
print("Сума парних чисел в діапазоні від 0 до 20 дорівює:",int(Sum))
print("Добуток не парних чисел в діапазоні від 0 до 20 дорівює:",int(product))

exit(0)