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
def main():
    if not os.path.exists(input_file):
        print("Вхідний файл не існує!")
        return
    with open(input_file, 'r', encoding='utf-8') as infile:
        text = infile.read()
    if word_to_find in text:
        result = f"Слово '{word_to_find}' знайдено у файлі."
    else:
        result = f"Слово '{word_to_find}' відсутнє у файлі."
    print(result)
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write(result + "\n")
if __name__ == "__main__":
    main()
