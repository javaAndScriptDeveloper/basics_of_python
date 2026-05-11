import sys
import datetime


def log_to_file(error_message):
    #Записує помилку у файл error.log з міткою часу
    with open("error.log", "a", encoding="utf-8") as f:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{now}] {error_message}\n")


try:
    print("Введіть список чисел через пробіл:")
    data = sys.stdin.read().strip()
    items = data.split()

    if not items:
        raise ValueError("Список порожній")

    numbers = [float(x) for x in items]
    print(f"Ваш список чисел: {numbers}")

except ValueError as e:
    # Обробка порожнього списку або некоректних символів
    msg = f"Помилка введення: {e}"
    print(msg)
    log_to_file(msg)

except Exception as e:
    # Обробка інших непередбачуваних помилок
    msg = f"Критична помилка: {e}"
    print(msg)
    log_to_file(msg)

finally:
    print("Виконання операції завершено.")