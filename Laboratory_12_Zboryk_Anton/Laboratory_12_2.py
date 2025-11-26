import os
import re
import csv

import pandas as pd
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


#Функція для завантаження текстів з файлу
def load_texts_from_file(path, column):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Файл не знайдено: {path}")


    ext = os.path.splitext(path)[1].lower()
    texts= []

    if ext == ".csv":
        # Читаємо CSV
        df = pd.read_csv(path)
        if column is None:
            # Якщо користувач не вказав колонку, пробуємо знайти підходящу
            candidates = ["text", "message", "content", "body"]
            found = []
            for column in df.columns:
                # Переводимо назву колонки у нижній регістр
                column_lower = column.lower()

                # Перевіряємо, чи хоч одне слово зі списку candidates входить у назву
                match = False
                for cand in candidates:
                    if cand in column_lower:
                        match = True
                        break
                if match:
                    found.append(column)
            if found:
                column = found[0]
                print(f"Знайдено колонку: {column}")
            else:
                column = df.columns[0]
                print(f"Колонку не знайдено, використовується перша: {column}")
        texts = df[column].dropna().astype(str).tolist()

    elif ext == ".txt":
        # Читаємо TXT
        with open(path, "r", encoding="utf-8") as f:
            texts = [line.strip() for line in f if line.strip()]
    else:
        raise ValueError("Підтримуються формати: CSV, TXT.")

    if not texts:
        raise ValueError("Файл прочитано, але тексти відсутні.")

    return texts


#Функція для вводу текстів вручну
def get_texts_from_user():
    print("Введіть тексти построчно. Порожній рядок — завершення.")
    texts = []
    while True:
        line = input().strip()
        if line == "":
            break
        texts.append(line)
    if not texts:
        raise ValueError("Не введено жодного тексту.")
    return texts


#Попередня обробка тексту
def preprocess_text(text):
    text = re.sub(r"http\S+|www\.\S+", " ", text)   # прибираємо посилання
    text = re.sub(r"@\w+", " ", text)               # прибираємо @користувачів
    text = re.sub(r"#(\w+)", r"\1", text)           # прибираємо #
    text = re.sub(r"\s+", " ", text).strip()        # прибираємо зайві пробіли
    return text


#Оцінка емоційного забарвлення
def emotional(score):
    if score >= 0.05:
        return "positive"
    elif score <= -0.05:
        return "negative"
    else:
        return "neutral"



analyzer = SentimentIntensityAnalyzer() #створюю змінну, щоб скоротити запис методу

def analyze_vader(text):
    scores = analyzer.polarity_scores(text)
    result = emotional(scores["compound"])
    return {
        "text": text,
        "neg": scores["neg"],
        "neu": scores["neu"],
        "pos": scores["pos"],
        "compound": scores["compound"],
        "result": result
    }


#Підрахунок статистики
def calculation_stats(results):
    total = len(results)
    counts = {"positive": 0, "neutral": 0, "negative": 0}
    for r in results:
        counts[r["result"]] += 1
    return {"total": total, **counts}


#Побудова графіка
def build_plot(stats, title):
    categories = ["negative", "neutral", "positive"]
    values = [stats.get("negative", 0), stats.get("neutral", 0), stats.get("positive", 0)]

    fig, ax = plt.subplots()
    ax.bar(categories, values, color=["red", "blue", "green"])
    ax.set_title(title)
    ax.set_ylabel("Кількість")
    for i, v in enumerate(values):
        ax.text(i, v + 0.1, str(v), ha="center")
    fig.tight_layout()
    return fig

def save_results(results, stats, plot_fig, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    output_csv = os.path.join(out_dir, "results.csv")
    output_txt = os.path.join(out_dir, "stats.txt")
    output_png = os.path.join(out_dir, "distribution.png")

    df = pd.DataFrame(results)
    df.to_csv(output_csv, index=False, quoting=csv.QUOTE_MINIMAL)

    with open(output_txt, "w", encoding="utf-8") as f:
        f.write("Результат:\n")
        for k, v in stats.items():
            f.write(f"{k}: {v}\n")

    plot_fig.savefig(output_png)

    return output_csv, output_txt, output_png

#Основна програма
def main():
    print("Аналіз тональності текстових повідомлень (VADER)")
    print("1) Файл (CSV/TXT)")
    print("2) Ввід вручну")
    choice = input("Ваш вибір (1 або 2): ").strip()

    try:
        if choice == "1":
            path = input("Вкажіть шлях до файлу: ").strip()
            column = input("Назва колонки для CSV (Enter, якщо не знаєте): ").strip() or None
            texts = load_texts_from_file(path, column)
        elif choice == "2":
            texts = get_texts_from_user()
        else:
            print("Некоректний вибір.")
            return
    except Exception as e:
        print(f"Помилка імпорту: {e}")
        return

    print(f"Завантажено {len(texts)} текст(ів). Виконується очищення...")
    texts_clean = [preprocess_text(t) for t in texts]

    print("Виконується аналіз...")
    results = [analyze_vader(t) for t in texts_clean]

    stats = calculation_stats(results)
    print("Результати аналізу")
    print(f"Всього текстів: {stats['total']}")
    print(f"Позитивних: {stats['positive']}")
    print(f"Нейтральних: {stats['neutral']}")
    print(f"Негативних: {stats['negative']}")

    print("Побудова графіка:")
    fig = build_plot(stats, title="Розподіл тональності")
    plt.show()  # показуємо графік на екрані
    out_dir = input("Вкажіть директорію для збереження (наприклад, output): ").strip() or "output"

    try:
        output_csv, output_txt, output_png = save_results(results, stats, fig, out_dir)
        print("Збережено файли:")
        print(f"{output_csv}")
        print(f"{output_txt}")
        print(f"{output_png}")
    except Exception as e:
        print(f"Помилка збереження результатів: {e}")
        return
    print("Готово!")

main()
