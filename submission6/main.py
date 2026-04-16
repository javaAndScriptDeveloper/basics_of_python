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

# Шляхи до файлів (згідно з даними для завдання та bash-скриптом варіанту 10)
input_json = "students.json"
input_json2 = "students2.json"

def compare_json_files(file1, file2):
    # Зчитування даних з першого файлу
    try:
        with open(file1, 'r', encoding='utf-8') as f:
            data1 = json.load(f)
    except FileNotFoundError:
        print(f"Помилка: файл {file1} не знайдено.")
        return

    # Зчитування даних з другого файлу
    try:
        with open(file2, 'r', encoding='utf-8') as f:
            data2 = json.load(f)
    except FileNotFoundError:
        print(f"Помилка: файл {file2} не знайдено.")
        return

    # Перетворюємо списки словників у словники словників для зручного порівняння.
    # В якості ключа використовуємо 'name', оскільки це унікальний ідентифікатор студента.
    dict1 = {student['name']: student for student in data1}
    dict2 = {student['name']: student for student in data2}

    print("=== Результати порівняння файлів ===")
    
    # 1. Шукаємо змінені або видалені записи (ті, що є в dict1)
    for name, info1 in dict1.items():
        if name not in dict2:
            print(f"[-] Видалено студента: {name}")
        elif info1 != dict2[name]:
            print(f"[*] Змінено дані студента: {name}")
            # Можна також вивести конкретні зміни, але для тесту достатньо імені
            print(f"    Було:  {info1}")
            print(f"    Стало: {dict2[name]}")

    # 2. Шукаємо нові (додані) записи (ті, що є тільки в dict2)
    for name, info2 in dict2.items():
        if name not in dict1:
            print(f"[+] Додано нового студента: {name}")

if __name__ == "__main__":
    compare_json_files(input_json, input_json2)