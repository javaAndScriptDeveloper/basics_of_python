import json

# Шляхи до файлів
input_json = "students.json"
search_name = "Марія"

try:
    with open(input_json, 'r', encoding='utf-8') as f:
        students = json.load(f)

    found = False
    #Пошук студента за ім'ям
    for student in students:
        if student["name"] == search_name:
            # Виводимо дані, як того очікує скрипт перевірки
            print(f"Знайдено студента: {student['name']}, Вік: {student['age']}, Факультет: {student['faculty']}")
            found = True
            break

    if not found:
        print(f"Студента з ім'ям {search_name} не знайдено.")

except FileNotFoundError:
    print(f"Помилка: Файл {input_json} не знайдено.")
except json.JSONDecodeError:
    print("Помилка: Файл має некоректний формат JSON.")