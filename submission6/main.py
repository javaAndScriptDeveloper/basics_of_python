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
def read_info(input_file):
    try:
        with open(input_file, "r", encoding="utf-8") as file:
            sts = json.load(file)
            print(f"{'Ім’я':<20} | {'Вік':<5} | {'Факультет'}")
            print("-" * 40)
            for st in sts:
                name = st.get("name")
                age = st.get("age")
                faculty = st.get("faculty")
                print(f"{name:<20} | {age:<5} | {faculty}")

    except FileNotFoundError:
        print(f"Помилка: Файл {input_file} не знайдено.")
    except json.JSONDecodeError:
        print("Помилка: Файл має некоректний формат JSON.")

    except Exception as e:
        print(f"Сталася непередбачена помилка: {e}")
read_info(input_json)
