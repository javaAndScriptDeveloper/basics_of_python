# Дані для завдання

# Словник для перевірки (варіант 6)
data = {"name": "Олена", "age": 20, "faculty": "КН"}

# Файл для запису помилок (варіант 8)
error_file = "error.log"

# Файл для зчитування (варіанти 5, 9)
input_file = "input.txt"

# Формат даних у файлі (варіант 9): "ім'я:вік" у кожному рядку

import logging

logging.basicConfig(filename="error.log", level=logging.ERROR)

try:
    # Зчитуємо рядок і перетворюємо на список чисел
    line = input("Введіть числа через пробіл: ").strip()

    if not line:
        raise ValueError("Порожній список — не введено жодного числа")

    numbers = [float(x) for x in line.split()]

    # Виводимо числа
    print(*numbers)

except ValueError as e:
    # Обробка винятку порожнього або некоректного списку
    msg = f"Помилка: {e}"
    print(msg)
    logging.error(msg)
