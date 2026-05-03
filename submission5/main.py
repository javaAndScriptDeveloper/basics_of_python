# Дані для завдання

# Шлях до вхідного файлу
input_file = "input.txt.txt"

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

import os

if not os.path.exists(input_file):
    print(f"Файл {input_file} не знайдено.")
else:
    # Відкриваємо файл для читання
    with open(input_file, 'r', encoding='utf-8') as infile:
        data = infile.read().split()

    numbers = []
    for item in data:
        try:
            numbers.append(float(item))
        except ValueError:
            continue

    if not numbers:
        print("У файлі не знайдено числових даних для обчислення.")
    else:
        average = sum(numbers) / len(numbers)

        # Записуємо результат у вихідний файл
        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write(str(average))

        print(average)

