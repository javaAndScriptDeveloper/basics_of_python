import os
# Дані для завдання

# Словник для перевірки (варіант 6)
data = {"name": "Олена", "age": 20, "faculty": "КН"}

# Файл для запису помилок (варіант 8)
error_file = "error.log"

# Файл для зчитування (варіанти 5, 9)
input_file = "input.txt"

# Формат даних у файлі (варіант 9): "ім'я:вік" у кожному рядку

# Реалізуйте завдання тут
def main():
    with open(error_file, "w", encoding="utf-8") as log:
        log.write("--- Log started ---\n")
    try:
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Файл {input_file} не знайдено")
        with open(input_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
        if not lines:
            print("Файл порожній.")
            return
        print("Зчитування даних:")
        for line_num, line in enumerate(lines, 1):
            line = line.strip()
            if not line: continue
            try:
                if ":" not in line:
                    raise ValueError(f"Некоректний формат у рядку {line_num}: '{line}'")
                name, age = line.split(":")
                age = int(age)
                print(f"Рядок {line_num}: Ім'я - {name}, Вік - {age}")
            except ValueError as e:
                error_msg = f"Помилка даних: {e}"
                print(error_msg)
                with open(error_file, "a", encoding="utf-8") as log:
                    log.write(error_msg + "\n")
    except FileNotFoundError as e:
        error_msg = f"Критична помилка: {e}"
        print(error_msg)
        with open(error_file, "a", encoding="utf-8") as log:
            log.write(error_msg + "\n")
    except Exception as e:
        error_msg = f"Непередбачена помилка: {e}"
        print(error_msg)
        with open(error_file, "a", encoding="utf-8") as log:
            log.write(error_msg + "\n")
    else:
        print("Основне зчитування завершено успішно.")
    finally:
        print("Завершення обробки файлу.")
if __name__ == "__main__":
    main()
