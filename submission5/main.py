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
# ==========================================
# РЕАЛІЗАЦІЯ ЗАВДАННЯ (Варіант 6)
# ==========================================
import os
print("--- Індивідуальне завдання (Варіант 6) ---")

# Перевіряємо, чи існує вхідний файл
if not os.path.exists(input_file):
    print(f"Помилка: Файл '{input_file}' не знайдено. Створіть його та додайте текст.")
else:
    # Відкриваємо файл для читання за допомогою безпечної конструкції with
    with open(input_file, 'r', encoding='utf-8') as infile:
        content = infile.read()  # Зчитуємо весь вміст файлу як один рядок
    
    # Виконуємо заміну слова
    updated_content = content.replace(word_to_replace, replacement_word)
    
    # Відкриваємо новий файл для запису (режим 'w' створить новий або перезапише існуючий)
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write(updated_content)  # Записуємо оновлений текст
        
    print(f"Обробка завершена! Усі входження слова '{word_to_replace}' замінено на '{replacement_word}'.")
    print(f"Результат збережено у файлі '{output_file}'.")