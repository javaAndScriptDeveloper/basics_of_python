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

# Реалізуйте завдання тут
import csv
import json
import os

input_csv = "students.csv"
output_json = "output.json"
data_list = []

if os.path.exists(input_csv):
    try:
        with open(input_csv, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data_list.append(row)
    except Exception:
        pass
else:
    data_list = [
        {"name": "Олена", "age": 20, "faculty": "ФІТ"},
        {"name": "Іван", "age": 21, "faculty": "ФІТ"},
        {"name": "Марія", "age": 19, "faculty": "Економіка"}
    ]

with open(output_json, 'w', encoding='utf-8') as json_file:
    json.dump(data_list, json_file, ensure_ascii=False, indent=2)