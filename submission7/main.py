# Дані для завдання

# Словник для перевірки (варіант 6)
data = {"name": "Олена", "age": 20, "faculty": "КН"}

# Файл для запису помилок (варіант 8)
error_file = "error.log"

# Файл для зчитування (варіанти 5, 9)
input_file = "input.txt"

# Формат даних у файлі (варіант 9): "ім'я:вік" у кожному рядку

# Реалізуйте завдання тут
import datetime
try:
    num = float(input("Введіть ділене (число, яке ділимо): "))
    den = float(input("Введіть дільник (число, на яке ділимо): "))
    result = num / den
    print(f"Результат: {num} / {den} = {result}")

except ZeroDivisionError as e:
    cur_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    error_msg = f"[{cur_time}] Ділення на нуль неможливе! (Деталі: {e})"
    print(error_msg)
    with open(error_file, "a", encoding="utf-8") as log_file:
        log_file.write(error_msg + "\n")

except ValueError as e:
    cur_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    error_msg = f"[{cur_time}] Помилка типу даних (Деталі: {e})"
    print(error_msg)
    with open(error_file, "a", encoding="utf-8") as log_file:
        log_file.write(error_msg + "\n")
