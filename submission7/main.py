from datetime import datetime

# Файл для зчитування
input_file = "input.txt"

# Лог-файл
log_file = "lab7_log.txt"


class EmptyFileError(Exception):
    """Користувацький виняток для порожнього файлу"""
    pass


def log_exception(e):
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} - {type(e).__name__}: {e}\n")


try:
    with open(input_file, "r", encoding="utf-8") as f:
        data = f.read()

    if not data.strip():
        raise EmptyFileError("Файл порожній")

except FileNotFoundError as e:
    print("Помилка: файл не знайдено")
    log_exception(e)

except PermissionError as e:
    print("Помилка: немає доступу до файлу")
    log_exception(e)

except UnicodeDecodeError as e:
    print("Помилка: проблема з кодуванням файлу")
    log_exception(e)

except EmptyFileError as e:
    print(f"Помилка: {e}")
    log_exception(e)

except Exception as e:
    print(f"Невідома помилка: {e}")
    log_exception(e)

else:
    print("Файл успішно прочитано:")
    print(data)

finally:
    print("Програма завершила роботу")