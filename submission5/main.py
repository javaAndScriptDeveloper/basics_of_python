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
def rewrite_file(input_file, output_file):
    try:
        with open(input_file, "r", encoding='utf-8') as infile, \
            open(output_file, "w", encoding='utf-8') as outfile:
            for line in infile:
                trans=line.lower()
                outfile.write(trans)
        print(f"Файл {input_file} перезаписано {output_file}")
    except FileNotFoundError:
        print(f"Файл {input_file} не знайдено")
    except Exception as e:
        print(e)
rewrite_file(input_file, output_file)
