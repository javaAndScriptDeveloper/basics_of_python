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
    a = float(input())
    b = float(input())
    result = a / b
    print(result)
except ValueError as e:
    with open(error_file, 'a') as f:
        f.write(f"ValueError: {e}\n")
    print("Помилка: введено некоректні дані.")
except ZeroDivisionError as e:
    with open(error_file, 'a') as f:
        f.write(f"ZeroDivisionError: {e}\n")
    print("Помилка: ділення на нуль.")
except Exception as e:
    with open(error_file, 'a') as f:
        f.write(f"Exception: {e}\n")
    print("Сталася помилка.")