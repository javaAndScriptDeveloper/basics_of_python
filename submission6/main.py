import json
import os

# Шляхи до файлів
input_json = "students.json"
output_json = "output.json"

# Дані для зміни (варіант 4): змінити факультет студента
student_to_update = "Іван"
new_faculty = "КН"

# Базові дані на випадок, якщо файлу ще не існує (щоб програма не падала)
default_students = [
    {"name": "Олена", "age": 20, "faculty": "КН"},
    {"name": "Іван", "age": 22, "faculty": "ІТ"},
    {"name": "Марія", "age": 19, "faculty": "КН"}
]

# 1. Перевірка та створення вхідного файлу, якщо його немає
if not os.path.exists(input_json):
    try:
        with open(input_json, "w", encoding="utf-8") as file:
            json.dump(default_students, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Помилка при створенні файлу: {e}")

# 2. Основна логіка - Зчитування, зміна та запис у НОВИЙ файл
try:
    # Зчитуємо дані з вхідного файлу
    with open(input_json, "r", encoding="utf-8") as file:
        students = json.load(file)
    
    student_found = False
    
    # Шукаємо студента за ім'ям та змінюємо факультет
    for student in students:
        if student.get("name") == student_to_update:
            student["faculty"] = new_faculty
            student_found = True
            break
            
    if not student_found:
        print(f"Студента з ім'ям '{student_to_update}' не знайдено у файлі.")
        
    # Записуємо оновлені дані у ВИХІДНИЙ файл (output.json), як вимагає тест
    with open(output_json, "w", encoding="utf-8") as file:
        json.dump(students, file, ensure_ascii=False, indent=4)
        
    print(f"Зміни успішно збережено у файл '{output_json}'!")

except Exception as e:
    print(f"Виникла помилка: {e}")