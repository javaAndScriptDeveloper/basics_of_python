# Дані для завдання

# Шлях до вхідного файлу
input_file = "input.txt"

# Шлях до вихідного файлу
output_file = "output.txt"

# Слово для пошуку (варіант 5)
word_to_find = "Python"

# Слово для заміни та нове слово (варіант 6)
word_to_replace = "World"
replacement_word = "Ukraine"

# Новий рядок для додавання (варіант 7)
new_line = "Новий рядок додано"

# Новий вміст для перезапису (варіант 10)
new_content = "Файл перезаписано"

# Реалізуйте завдання тут
# Лабораторна робота №5
# Варіант 6
# Заміна слова у текстовому файлі

import os

# Слова для заміни
word_to_replace = "World"
replacement_word = "Ukraine"

# Перевірка існування файлу
if not os.path.exists("input.txt"):
    print("Файл input.txt не знайдено. Створіть файл та додайте текст.")
else:
    # Читання файлу
    with open("input.txt", "r", encoding="utf-8") as infile:
        text = infile.read()

    # Заміна слова
    new_text = text.replace(word_to_replace, replacement_word)

    # Запис у новий файл
    with open("output.txt", "w", encoding="utf-8") as outfile:
        outfile.write(new_text)

    print("Заміна виконана. Результат збережено у файлі output.txt")
