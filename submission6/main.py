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

def compare_json_files(file1, file2):
    """Compare two JSON files and output differences."""
    try:
        with open(file1, 'r', encoding='utf-8') as f:
            data1 = json.load(f)
        with open(file2, 'r', encoding='utf-8') as f:
            data2 = json.load(f)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return

    # Extract names from both files
    names1 = {student["name"] for student in data1}
    names2 = {student["name"] for student in data2}

    # Find differences
    added = names2 - names1  # in file2 but not in file1
    removed = names1 - names2  # in file1 but not in file2
    common = names1 & names2

    # Output differences
    differences = list(added | removed)
    if differences:
        print("|".join(sorted(differences)))

# Run comparison
compare_json_files(input_json, input_json2)
