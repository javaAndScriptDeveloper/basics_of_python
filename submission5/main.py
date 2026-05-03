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


def replace_World_with_Ukraine(input_filename, output_filename):
    file_lines = get_lines_from_input_file(input_filename)
    replace_words(file_lines, word_to_replace, replacement_word)
    make_output_file(output_filename, file_lines)


def get_lines_from_input_file(input_filename):
    if not os.path.exists(input_filename):
        return None
    
    with open(input_filename, 'r') as incoming_file:
        file_lines = incoming_file.readlines()
    return file_lines


def replace_words(string_lines, initial_word, replacement_word):
    for i in range(len(string_lines)):
        string_lines[i] = string_lines[i].replace(initial_word, replacement_word)


def make_output_file(output_filename, string_lines):
    with open(output_filename, 'w') as output_file:
        output_file.writelines(string_lines)


replace_World_with_Ukraine(input_file, output_file)
