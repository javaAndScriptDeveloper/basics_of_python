# Дані для завдання

# Словник для перевірки (варіант 6)
data = {"name": "Олена", "age": 20, "faculty": "КН"}

# Файл для запису помилок (варіант 8)
error_file = "error.log"

# Файл для зчитування (варіанти 5, 9)
input_file = "input.txt"

# Формат даних у файлі (варіант 9): "ім'я:вік" у кожному рядку

# Реалізуйте завдання тут
logging.basicConfig(filename=error_file, level=logging.ERROR)

try:
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    valid_names = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        parts = line.split(':')
        if len(parts) != 2:
            raise ValueError("Некоректна кількість параметрів у рядку.")
        
        name = parts[0]
        age_str = parts[1]
        
        # Перевіряємо, чи вік є числом 
        age = int(age_str) 
        
        valid_names.append(name)
        
    print(" ".join(valid_names))

except FileNotFoundError as e:
    print("Помилка: Файл не знайдено.")
    logging.error(f"FileNotFoundError: {e}")
except ValueError as e:
    print(f"Помилка формату даних у файлі: {e}")
    logging.error(f"ValueError: {e}")
except Exception as e:
    print("Невідома помилка.")
    logging.error(f"Exception: {e}")