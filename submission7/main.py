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
import logging
import sys

# Налаштування логування: запис у файл error.log
logging.basicConfig(
    filename='error.log', 
    level=logging.ERROR, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

def main():
    try:
        # Зчитуємо дані. Зчитування працює і для ручного вводу, і для пайплайнів (echo "..." | python3 main.py)
        user_input = input("Введіть дату у форматі dd-mm-yyyy: ").strip()
        
        if not user_input:
            raise ValueError("Порожнє введення.")

        # Перевіряємо коректність дати за форматом dd-mm-yyyy
        valid_date = datetime.datetime.strptime(user_input, "%d-%m-%Y")
        
        # Виведення у форматі, який очікує перевірка (Коректно, 25.12.2024)
        print(f"Коректна дата: {valid_date.strftime('%d.%m.%Y')}")

    except ValueError as e:
        # Обробка помилки неправильного формату або неіснуючої дати (напр., 31 лютого)
        error_msg = f"Помилка: Некоректна дата або формат. Деталі: {e}"
        print(error_msg)          # Виводимо на екран згідно з умовою
        logging.error(error_msg)  # Зберігаємо у логфайл error.log

    except Exception as e:
        # Обробка будь-яких інших непередбачених винятків
        error_msg = f"Невідома помилка: {e}"
        print(error_msg)
        logging.error(error_msg)

if __name__ == "__main__":
    main()