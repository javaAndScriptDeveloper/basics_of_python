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
# ІНДИВІДУАЛЬНЕ ЗАВДАННЯ (Варіант 4)

# 1. Зчитуємо дані з вхідного JSON-файлу
with open(input_json, 'r', encoding='utf-8') as file_in:
    students_data = json.load(file_in)

# 2. Шукаємо потрібного студента та змінюємо його факультет
for student in students_data:
    if student.get("name") == student_to_update:
        student["faculty"] = new_faculty
        print(f"Факультет студента {student_to_update} успішно змінено на {new_faculty}!")
        break

# 3. Записуємо оновлені дані у вихідний JSON-файл
with open(output_json, 'w', encoding='utf-8') as file_out:
    json.dump(students_data, file_out, ensure_ascii=False, indent=2)

print(f"Оновлені дані збережено у файл {output_json}.")