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

#Перевіряю 2 можливих назви, адже Локальна перевірка та Git не співпадають
if os.path.exists('input.txt.txt'):
    input_filename = 'input.txt.txt'
elif os.path.exists('input.txt'):
    input_filename = 'input.txt'
else:
    input_filename = None

if input_filename is None:
    print("Error: Input file not found (checked input.txt and input.txt.txt)")
else:
    try:
        with open(input_filename, 'r', encoding='utf-8') as f:
            data = f.read().split()

        numbers = [float(x) for x in data]

        if numbers:
            average = sum(numbers) / len(numbers)

            with open('output.txt', 'w', encoding='utf-8') as out:
                out.write(str(average))

            print(average)
    except Exception as e:
        print(f"Error: {e}")
