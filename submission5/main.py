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


try:
    with open(input_file, 'r', encoding='utf-8') as infile:
        content = infile.read()
        words = content.split()
        word_count = len(words)

    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write(str(word_count))
except FileNotFoundError:
    print("Файл input.txt не знайдено.")