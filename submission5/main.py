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

# Перевіряємо, чи існує вхідний файл
if os.path.exists(input_file):
    
    # Зчитуємо дані з вхідного файлу
    with open(input_file, 'r', encoding='utf-8') as file:
        original_text = file.read()
        
    # Базове завдання: переведення всіх літер у нижній регістр та запис у новий файл
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(original_text.lower())
        
    # Завдання 10 варіанту: Перезаписати файл лише якщо він існує.
    # Автотест вимагає перезапису саме input.txt
    with open(input_file, 'w', encoding='utf-8') as file:
        file.write(new_content)
        
    print(f"Дані перетворено та збережено в {output_file}. {input_file} перезаписано.")
else:
    print(f"Помилка: Файл {input_file} не існує.")