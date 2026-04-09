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

# Дані про курси (варіант 6)
courses = [
    {"name": "Python програмування", "faculty": "КН", "credits": 5},
    {"name": "Бази даних", "faculty": "ІТ", "credits": 4},
    {"name": "Алгоритми", "faculty": "ФМ", "credits": 6}
]

# Примітка: при запису JSON використовуйте ensure_ascii=False
# json.dump(data, f, ensure_ascii=False, indent=2)

# Реалізуйте завдання тут
# Лабораторна робота №6
# Варіант 6
# Сортування курсів за кількістю кредитів та запис у JSON

import json

# Дані
courses = [
    {"name": "Python програмування", "faculty": "КН", "credits": 5},
    {"name": "Бази даних", "faculty": "ІТ", "credits": 4},
    {"name": "Алгоритми", "faculty": "ФМ", "credits": 6}
]

# Сортування за credits
sorted_courses = sorted(courses, key=lambda x: x["credits"])

# Вивід на екран
print("Відсортовані курси:")
for course in sorted_courses:
    print(f"{course['name']} - {course['credits']} кредитів")

# Запис у JSON файл
with open("courses_sorted.json", "w", encoding="utf-8") as f:
    json.dump(sorted_courses, f, ensure_ascii=False, indent=2)

print("\nДані збережено у файлі courses_sorted.json")