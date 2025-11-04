#Розробити програму, яка:
# а) створює текстовий файл TF12_1 із символьних рядків різної довжини;
# б) читає вміст файла TF12_1 і записує його у файл TF12_2 по рядках: у першому – один символ, у другому – два символи, … ,
# у десятому – десять символів, у одинадцятому – один символ і т. д. (останній рядок може бути не повним);
# в) читає вміст файла TF12_2 і друкує його по рядках.

import random



inputFileName1 = "TF12_1.txt"
inputFileName2 = "TF12_2.txt"
inputFileOK = False

#а)
while not inputFileOK:
    try:
        open(inputFileName1, "w+")
    except IOError:
        print("Файл: ", inputFileName1, "не може бути відкритим")
    else:
        print("Відкриття файлу: ", inputFileName1, " для читання та запису інформації.")
        inputFileOK = True
        if inputFileOK:
            print("Успішне відкриття файлу", inputFileName1)
            open(inputFileName1, "w+").close()
            with open(inputFileName1, "a+") as inputFile1:
                letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
                try:
                    for i in range(random.randint(5, 20)):
                        word = ""
                        for j in range(random.randint(1, 20)):
                            word += random.choice(letters)
                        inputFile1.write(word + "\n")

                except IOError:
                    print("Помилка із додаванням інформації у файл")
        else:
            print("Помилка у відкритті файлу! Аварійне завершення програми!", inputFileName1)
#б)
inputFileOK = False
while not inputFileOK:
    try:
        open(inputFileName2, "w+")
    except IOError:
        print("Файл: ", inputFileName2, "не може бути відкритим")
    else:
        print("Відкриття файлу: ", inputFileName2, " для читання та запису інформації.")
        inputFileOK = True
        if inputFileOK:
            print("Успішне відкриття файлу", inputFileName2)
            open(inputFileName2, "w+").close()
            try:
                with open(inputFileName2, "a+") as inputFile2, open(inputFileName1, "r+") as inputFile1:
                    data = inputFile1.read()
                    data = data.replace("\r", "").replace("\n", "")  # прибираємо всі переноси
                    i = 0
                    k = 1
                    while i < len(data):
                        inputFile2.write(data[i:i + k] + "\n")
                        i += k
                        k = k + 1 if k < 10 else 1

            except IOError:
                print("Помилка із додаванням інформації у файл")
            try:     #в)
                with open(inputFileName2, "r+") as inputFile2:
                    for data in inputFile2:
                        print(data, end="")
            except IOError: print("Помилка у зчитуванні файлу!")
        else:
            print("Помилка у відкритті файлу! Аварійне завершення програми!", inputFileName2)




print("Файл закритий", inputFileName1)

print("Файл закритий", inputFileName2)