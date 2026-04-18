# Дані для завдання

# Файл для запису помилок (варіант 8)
error_file = "error.log"

# Реалізуйте завдання тут
import os
from datetime import datetime

def log_error(message):
    """Функція для ручного запису помилки у файл з відміткою часу"""
    with open(error_file, "a", encoding="utf-8") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] ERROR: {message}\n")

def safe_division():
    """Програма для безпечного ділення"""
    try:
        #Введення даних
        num1= float(input("Введіть перше число:"))
        num2 = float(input("Введіть друге число:"))

        result = num1 / num2
        print(f"Результат: {result}")

    except ZeroDivisionError as e:
        error_msg = f"Ділення на нуль: {e}"
        print(error_msg)
        log_error(error_msg)

    except ValueError as e:
        error_msg = f"Помилка типу даних: {e}"
        print(error_msg)
        log_error(error_msg)

    finally:
        print("Операцію завершено")

if __name__ == "__main__":
    safe_division()

