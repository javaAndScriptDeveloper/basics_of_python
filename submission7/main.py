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
def log_error(message):
    """Записує повідомлення про помилку у лог-файл"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(error_file, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")

def divide(a, b):
    """Ділення двох чисел з обробкою винятку"""
    try:
        result = a / b
    except ZeroDivisionError:
        message = f"Помилка: ділення на нуль! ({a} / {b})"
        print(message)
        log_error(message)
        return None
    else:
        print(f"Результат: {a} / {b} = {result}")
        return result
    finally:
        print("Операція завершена.\n")

# Тестові виклики
divide(10, 2)    # Коректне ділення
divide(5, 0)     # Ділення на нуль
divide(100, 4)   # Коректне ділення
divide(7, 0)     # Ділення на нуль