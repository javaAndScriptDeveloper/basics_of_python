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


if not os.path.exists(input_file):
    print("Файл не знайдено")
else:
    total = 0
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
           
            content = infile.read()
           
            data = content.split()
            
            for item in data:
                total += int(item)
        
        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write(str(total))
            
        print(total/5)

    except ValueError:
        print("Помилка: у файлі не число")
    except Exception as e:
        print(f"Виникла помилка: {e}")
            