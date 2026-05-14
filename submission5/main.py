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

def solve():
    input_filename = "input.txt"
    output_filename = "output.txt"

    # Перевіряємо, чи існує вхідний файл
    if not os.path.exists(input_filename):
        return

    # 1. Зчитування даних з текстового файлу
    with open(input_filename, "r") as file:
        # Зчитуємо рядки, видаляємо зайві пробіли та перетворюємо на числа
        content = file.readlines()
        numbers = []
        for line in content:
            stripped = line.strip()
            if stripped:  # Пропускаємо порожні рядки
                numbers.append(int(stripped))

    # 2. Виконання перетворення (сортування)
    numbers.sort()

    # 3. Запис результатів у новий файл
    with open(output_filename, "w") as file:
        # Записуємо кожне число з нового рядка
        for num in numbers:
            file.write(f"{num}\n")

if __name__ == "__main__":
    solve()