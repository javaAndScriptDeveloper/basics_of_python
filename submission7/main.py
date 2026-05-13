# Дані для завдання

# Словник для перевірки (варіант 6)
data = {"name": "Олена", "age": 20, "faculty": "КН"}

# Файл для запису помилок (варіант 8)
error_file = "error.log"

# Файл для зчитування (варіанти 5, 9)
input_file = "input.txt"

# Формат даних у файлі (варіант 9): "ім'я:вік" у кожному рядку

# Реалізуйте завдання тут
# Варіант 4
import datetime

# 1. Власний клас винятку 
class NegativeNumberError(Exception):
    pass

# 2. Функція для логування 
def log_error(msg):
    with open(error_file, 'a', encoding='utf-8') as f:
        time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{time_now}] {msg}\n")

# 3. Основна логіка перевірки
try:
    user_input = input("Введіть число: ")
    num = float(user_input)
    
    if num < 0:
        # Викликаємо твій персональний виняток
        raise NegativeNumberError(f"Число {num} менше нуля!")
    
    print(f"Результат: Число {num} успішно пройшло перевірку.")

except ValueError:
    error_msg = f"ValueError: '{user_input}' не є числом."
    print(f"Помилка: {error_msg}")
    log_error(error_msg)

except NegativeNumberError as e:
    error_msg = f"NegativeNumberError: {e}"
    print(f"Помилка: {error_msg}")
    log_error(error_msg)

finally:
    print("Перевірка завершена.")