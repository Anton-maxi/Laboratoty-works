#Імпортувати бібліотеку NLTK та тексти із електронного архіву текстів Project Gutenberg,
# для виконання завдань взяти текст, заданий варіантом.
#Визначити кількість слів у тексті.
# Визначити 10 найбільш вживаних слів у тексті, побудувати на основі цих даних стовпчасту діаграму.
# Виконати видалення з тексту стоп-слів та пунктуації, після чого знову знайти 10 найбільш вживаних слів
# у тексті та побудувати на їх основі стовпчасту діаграму.



from nltk.corpus import gutenberg, stopwords
from nltk.probability import FreqDist
import string
import matplotlib.pyplot as plt


# 1. Імпортувати текст chesterton-ball.txt
words = gutenberg.words('chesterton-ball.txt')

# 2. Визначити кількість слів у тексті
print("Кількість слів у тексті:", len(words))

# 3. Визначити 10 найбільш вживаних слів
fdist = FreqDist(words)
top10 = fdist.most_common(10)
print("10 найбільш вживаних слів (без очищення):")
print(top10)

# Побудова стовпчастої діаграми
labels, counts = zip(*top10)
plt.figure(figsize=(10,5))
plt.bar(labels, counts, color="skyblue")
plt.title("10 найбільш вживаних слів (оригінальний текст)")
plt.xlabel("Слова")
plt.ylabel("Частота")
plt.show()


# 4. Видалення стоп-слів та пунктуації
stop_words = set(stopwords.words('english'))
punct = set(string.punctuation)

filtered_words = [w.lower() for w in words if w.lower() not in stop_words and w not in punct]

# 5. Знову знайти 10 найбільш вживаних слів після очищення
fdist_clean = FreqDist(filtered_words)
top10_clean = fdist_clean.most_common(10)
print("10 найбільш вживаних слів (після очищення):")
print(top10_clean)

# Побудова стовпчастої діаграми
labels_clean, counts_clean = zip(*top10_clean)
plt.figure(figsize=(10,5))
plt.bar(labels_clean, counts_clean, color="orange")
plt.title("10 найбільш вживаних слів (очищений текст)")
plt.xlabel("Слова")
plt.ylabel("Частота")
plt.show()










