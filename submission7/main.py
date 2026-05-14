import sys


def solve():
    log_file = "error.log"

    try:
        # 1. Зчитування даних (використовуємо stdin для надійності в Docker)
        input_data = sys.stdin.read().split()
        if len(input_data) < 2:
            return

        a = float(input_data[0])
        b = float(input_data[1])

        # 2. Виконання операції
        result = a / b

        # Вивід результату (якщо все ок)
        # Використовуємо int(result) якщо це ціле число, щоб відповідати патерну "2" для "10 5"
        if result.is_integer():
            print(int(result))
        else:
            print(result)

    except ZeroDivisionError as e:
        # 3. Обробка винятку: вивід на екран
        error_msg = f"Помилка: ділення на нуль! ({e})"
        print(error_msg)

        # 4. Запис у лог-файл (обов'язкова умова тесту)
        with open(log_file, "w", encoding="utf-8") as f:
            f.write(error_msg)

    except ValueError as e:
        print(f"Помилка: некоректні дані! ({e})")
        with open(log_file, "w", encoding="utf-8") as f:
            f.write(str(e))

    except Exception as e:
        print(f"Непередбачена помилка: {e}")
        with open(log_file, "w", encoding="utf-8") as f:
            f.write(str(e))


if __name__ == "__main__":
    solve()