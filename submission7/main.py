# Дані для завдання
import logging
# Словник для перевірки (варіант 6)
data = {"name": "Олена", "age": 20, "faculty": "КН"}

# Файл для запису помилок (варіант 8)
error_file = "error.log"

# Файл для зчитування (варіанти 5, 9)
input_file = "input.txt"

# Формат даних у файлі (варіант 9): "ім'я:вік" у кожному рядку

# Реалізуйте завдання тут
logging.basicConfig(filename=error_file, level=logging.ERROR, 
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    encoding='utf-8')

class NegativeNumberError(Exception):
    pass

def check_positive(number):
    if number < 0:
        raise NegativeNumberError(f"Число {number} є від'ємним!")
    return number


def main():
    try:
        raw = input("Введіть число: ")
        number = float(raw)
        result = check_positive(number)
        print(f"Число {result} є невід'ємним.")

    except ValueError as e:
        msg = f"Введено не числове значення: '{raw}'"
        print(f"Помилка: {msg}")
        logging.error(msg)

    except NegativeNumberError as e:
        print(f"Помилка: {e}")
        logging.error(str(e))

    finally:
        print("Програму завершено.")


if __name__ == "__main__":
    main()