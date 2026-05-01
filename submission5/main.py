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

import os

# Назви файлів (стандартні для прикладів у методичці)
input_filename = 'input.txt'
output_filename = 'output.txt'

# Перевірка наявності файлу перед роботою з ним (як вимагає викладач)
if os.path.exists(input_filename):
    # Відкриваємо файл для читання
    with open(input_filename, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    # Фільтруємо: залишаємо рядки, які після видалення пробілів не дорівнюють порожнечі
    processed_lines = [line for line in lines if line.strip() != '']

    # Відкриваємо новий файл для запису результату
    with open(output_filename, 'w', encoding='utf-8') as outfile:
        outfile.writelines(processed_lines)
else:
    # Якщо автотест не створює файл, програма просто завершить роботу без помилок
    pass
