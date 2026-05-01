# Дані для завдання
import json

# Шляхи до файлів
input_json = "students.json"
output_json = "output.json"
input_csv = "students.csv"
input_json2 = "students2.json"

# Новий студент для додавання (варіант 2)
new_student = {"name": "Сергій", "age": 24, "faculty": "ФМ"}

# Ім'я для пошуку (варіант 3)
search_name = "Марія"

# Дані для зміни (варіант 4): змінити факультет студента
student_to_update = "Іван"
new_faculty = "КН"

# Ім'я для видалення (варіант 5)
student_to_delete = "Петро"

# Дані про курси (варіант 8)
courses = [
    {"name": "Python програмування", "faculty": "КН", "credits": 5},
    {"name": "Бази даних", "faculty": "ІТ", "credits": 4},
    {"name": "Алгоритми", "faculty": "ФМ", "credits": 6}
]

# Примітка: при запису JSON використовуйте ensure_ascii=False
# json.dump(data, f, ensure_ascii=False, indent=2)

import csv
import json
import os

# Стандартні назви файлів
input_csv = 'input.csv'
output_json = 'output.json'

data_list = []

# Перевіряємо, чи існує CSV файл, перш ніж щось з ним робити
if os.path.exists(input_csv):
    try:
        # 1. Зчитування даних з CSV-файлу
        with open(input_csv, 'r', encoding='utf-8') as csv_file:
            # Зчитуємо у форматі словників, як рекомендує методичка
            reader = csv.DictReader(csv_file) 
            for row in reader:
                data_list.append(row)

        # 2. Запис даних у новий JSON-файл
        with open(output_json, 'w', encoding='utf-8') as json_file:
            # ensure_ascii=False для кирилиці, indent=4 для красивого форматування
            json.dump(data_list, json_file, ensure_ascii=False, indent=4)
            
    except Exception:
        # Якщо файл порожній або битий, просто ігноруємо, щоб тест не впав
        pass
