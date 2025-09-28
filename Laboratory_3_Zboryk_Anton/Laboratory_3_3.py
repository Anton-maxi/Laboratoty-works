#Задано речення. Скласти програму, яка визначає і виводить на екран довжину його самого короткого слова
sentence= str(input("Введіть речення: "))
words=sentence.split()
dist= len(words[0])
result_word=words[0]
for i in range (len(words)):
    if dist>len(words[i]):
        dist= len(words[i])
        result_word = words[i]
print("Найкоротше слово в вашому реченні:",result_word,"\n", "Його довжина:", dist)