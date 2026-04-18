# Дані для завдання
import json, csv, os
import pandas as pd

# Шляхи до файлів
input_json = "students.json"
output_json = "output.json"
input_csv = "students.csv"
output_csv = "output_csv.csv"
output_excel = "result.xlsx"

# Дані про курси (варіант 8)
courses = [
    {"name": "Python програмування", "faculty": "КН", "credits": 5},
    {"name": "Бази даних", "faculty": "ІТ", "credits": 4},
    {"name": "Алгоритми", "faculty": "ФМ", "credits": 6}
]

# Примітка: при запису JSON використовуйте ensure_ascii=False
# json.dump(data, f, ensure_ascii=False, indent=2)

# Реалізуйте завдання тут

#Написати програму для створення JSON-файлу з інформацією про курси, які викладаються на факультеті.
#Робота з JSON
# Створення початкового файлу
with open(input_json, 'w', encoding="utf-8") as f:
    json.dump(courses, f, ensure_ascii=False, indent=2)
print(f"Файл {input_json} створено")

# Зчитування та модифікація JSON
if os.path.exists(input_json):
    with open(input_json, 'r', encoding="utf-8") as f:
        data = json.load(f)

    # Додаємо новий запис
    data.append({"name": "Фізичні основи комп'ютерних систем", "faculty": "ФМФ", "credits": 5})

    # Записуємо у новий файл
    with open(output_json, 'w', encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Дані JSON оброблено та збережено в {output_json}")

#Робота з CSV













