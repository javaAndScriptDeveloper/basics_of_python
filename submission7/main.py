import logging
import sys

# Налаштування логування
logging.basicConfig(
    filename='error.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)


def main():
    try:

        val1 = input("Введіть перше число: ")
        val2 = input("Введіть друге число: ")

        # Перевірка на порожні значення
        if not val1 or not val2:
            return

        num1 = float(val1)
        num2 = float(val2)

        # Виконання операції
        result = num1 / num2

        # Виведення результату
        if result == int(result):
            print(int(result))
        else:
            print(result)

    except ZeroDivisionError as e:
        error_message = "Помилка: ділення на нуль!"
        print(error_message)
        logging.error(f"{error_message} Деталі: {e}")

    except ValueError as e:
        error_message = "Помилка: введено не число!"
        print(error_message)
        logging.error(f"{error_message} Деталі: {e}")

    except Exception as e:

        error_message = f"Виникла непередбачена помилка: {e}"
        print(error_message)
        logging.error(error_message)


if __name__ == "__main__":
    main()