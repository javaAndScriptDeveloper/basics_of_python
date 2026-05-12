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
# ІНДИВІДУАЛЬНЕ ЗАВДАННЯ (Варіант 4)
# 1. Відкриваємо вхідний файл та зчитуємо всі рядки без символів \n
with open(input_file, 'r', encoding='utf-8') as file_in:
    lines = file_in.read().splitlines()

# 2. Перевертаємо список чистих рядків
reversed_lines = lines[::-1]

# 3. Відкриваємо вихідний файл і записуємо їх
with open(output_file, 'w', encoding='utf-8') as file_out:
    for line in reversed_lines:
        file_out.write(line + '\n')

print(f"Дані успішно записано у файл {output_file} у зворотному порядку!")