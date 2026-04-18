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
# Варіант 8: Записати список чисел у файл та відсортувати їх.
import os
input_file = "input.txt"
output_file = "output.txt"

# Перевіряємо, чи існує файл перед читанням
if os.path.exists(input_file):
    # Зчитуємо дані з вхідного файлу
    with open(input_file, 'r', encoding="utf-8") as infile:
        content = infile.read()
    # Перетворення даних: розбиваємо рядок на список окремих "слів", перетворюємо кожен рядок у ціле число
    try:
        numbers = [int(x) for x in content.split()]
        # Сортуємо список чисел
        numbers.sort()

        # Оскільки метод write приймає тільки рядки, перетворюємо числа назад у str
        sorted_content = " ".join([str(num) for num in numbers])

        # Запис результату у новий файл
        with open(output_file, 'w', encoding="utf-8") as outfile:
            outfile.write(sorted_content)

        print(f"Обробка завершена, відсортовані чиса збережено в {output_file}")
        print(f"Результат: {sorted_content}")

    except ValueError:
        print("Помилка")

else:
    print(f"Помилка: файл {input_file} не знайдено")
