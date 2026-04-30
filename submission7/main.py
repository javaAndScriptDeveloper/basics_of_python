# Дані для завдання

# Словник для перевірки (варіант 6)
data = {"name": "Олена", "age": 20, "faculty": "КН"}

# Файл для запису помилок (варіант 8)
error_file = "error.log"

# Файл для зчитування (варіанти 5, 9)
input_file = "input.txt"

# Формат даних у файлі (варіант 9): "ім'я:вік" у кожному рядку

# Реалізуйте завдання тут
try:
    a = float(input("Введіть число: "))

    if a < 0:
        raise ValueError("Введено від’ємне число!")

except ValueError as error:
    print(f"Помилка: {error}")

    with open(error_file, "a", encoding="utf-8") as log_file:
        log_file.write(f"Помилка: {error}\n")

else:
    print(f"Число коректне: {a}")

    with open(error_file, "a", encoding="utf-8") as log_file:
        log_file.write(f"Успішне введення: {a}\n")

finally:
    print("Програма завершила виконання.")

    with open(error_file, "a", encoding="utf-8") as log_file:
        log_file.write("Завершення програми\n")
