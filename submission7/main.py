import logging
import sys

logging.basicConfig(
    filename='error.log',
    level=logging.ERROR,
    format='%(asctime)s - %(message)s',
    encoding='utf-8'
)


def main():
    try:
        # Читаємо дані прямо з потоку 
        lines = sys.stdin.readlines()
        if len(lines) < 2:
            return

        num1 = float(lines[0].strip())
        num2 = float(lines[1].strip())

        result = num1 / num2

        # Виводимо тільки число
        if result == int(result):
            print(int(result))
        else:
            print(result)

    except ZeroDivisionError:

        msg = "Помилка: ділення на нуль"
        print(msg)
        logging.error(msg)
    except ValueError:
        print("Помилка: ValueError")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()