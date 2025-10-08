#Заповнити двовимірний масив розміром 7x7 таким чином, як показано на рисунку згідно з Вашим варіантом.
#Вивести масив на екран. Для виконання завдання використовуйте цикли.
matrix = [[0]*7 for i in range(7) ]
for i in range(7):
    for j in range(7):
        if i%2==0:
            if j%2 == 0:
                matrix[i][j]=1
            else:
                matrix[i][j]=0
        else:
            if j%2 == 0:
                matrix[i][j]=0
            else:
                matrix[i][j]=1
for i in range(0, 7):
    for j in range(0, 7):
        print(matrix[i][j], end=' ')
    print()

