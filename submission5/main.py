import os

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

# Check if input file exists
if not os.path.exists(input_file):
    print(f"Error: Input file '{input_file}' does not exist.")
else:
    # For variant 10: overwrite the input file with new content
    with open(input_file, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"File processed successfully. Input file '{input_file}' has been overwritten.")
