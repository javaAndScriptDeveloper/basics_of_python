import json
import os

# Шляхи до файлів (вже задані в шаблоні)
input_json = "students.json"
search_name = "Марія"

# 1. Перевіряємо, чи існує файл
if not os.path.exists(input_json):
    print(f"Помилка: Файл {input_json} не знайдено")
else:
    try:
        # 2. Відкриваємо та зчитуємо JSON
        with open(input_json, 'r', encoding='utf-8') as f:
            students = json.load(f)
        
        # 3. Шукаємо студента за ім'ям
        # Припускаємо, що students — це список словників
        found_student = None
        for student in students:
            if student.get("name") == search_name:
                found_student = student
                break
        
        # 4. Виводимо результат
        if found_student:
            # Використовуємо json.dumps для гарного виводу в консоль
            print(json.dumps(found_student, ensure_ascii=False, indent=2))
        else:
            print(f"Студента з ім'ям {search_name} не знайдено")

    except json.JSONDecodeError:
        print("Помилка: Некоректний формат JSON-файлу")
    except Exception as e:
        print(f"Виникла помилка: {e}")