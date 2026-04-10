import logging


logging.basicConfig(
    filename='error.log',
    level=logging.ERROR,
    format='%(asctime)s - %(message)s',
    encoding='utf-8'
)


def main():
    try:

        line1 = input()
        line2 = input()

        num1 = float(line1.strip())
        num2 = float(line2.strip())

        result = num1 / num2


        if result == int(result):
            print(int(result))
        else:
            print(result)

    except ZeroDivisionError:

        msg = "Помилка: ділення на нуль"
        print(msg)
        logging.error(msg)
    except Exception:

        print("Помилка")


if __name__ == "__main__":
    main()