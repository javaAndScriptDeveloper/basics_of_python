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
print("--- Індивідуальне завдання (Варіант 9) ---")

try:
    # Читаємо всі рядки з вхідного файлу
    with open(input_file, 'r', encoding='utf-8') as f_in:
        lines = f_in.readlines()

    # Залишаємо тільки ті рядки, які не є порожніми (strip прибирає пробіли/переноси)
    non_empty_lines = [line for line in lines if line.strip() != '']

    # Записуємо очищені рядки у вихідний файл
    with open(output_file, 'w', encoding='utf-8') as f_out:
        f_out.writelines(non_empty_lines)
        
    print("Порожні рядки успішно видалено.")
except FileNotFoundError:
    print("Вхідний файл не знайдено.")
