# Дані для завдання
import json
import os
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
print("--- Індивідуальне завдання (Варіант 6) ---")
print("Сортування студентів за віком і запис у новий JSON-файл.\n")

# Перевіряємо, чи існує вхідний файл
if not os.path.exists(input_json):
    print(f"❌ Помилка: Файл '{input_json}' не знайдено.")
    print("Будь ласка, створіть файл з тестовими даними.")
else:
    # 1. Зчитування даних з JSON-файлу
    with open(input_json, "r", encoding="utf-8") as file:
        students = json.load(file)  # JSON перетворюється на список словників
    
    print("📌 Початковий список студентів:")
    for student in students:
        print(f"Ім'я: {student['name']}, Вік: {student['age']}, Факультет: {student['faculty']}")
    
    # 2. Сортування студентів за віком
    # Використовуємо функцію sorted, де ключ сортування - це значення 'age' з кожного словника
    sorted_students = sorted(students, key=lambda x: x['age'])
    
    print("\n✅ Відсортований список студентів (за віком):")
    for student in sorted_students:
         print(f"Ім'я: {student['name']}, Вік: {student['age']}, Факультет: {student['faculty']}")
    
    # 3. Запис результату у новий JSON-файл
    with open(output_json, "w", encoding="utf-8") as file:
        # ensure_ascii=False гарантує правильне збереження кирилиці , indent=4 - гарне форматування [cite: 1965]
        json.dump(sorted_students, file, ensure_ascii=False, indent=4)
        
    print(f"\n📁 Дані успішно відсортовано та збережено у файл '{output_json}'.")