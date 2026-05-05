import json

# Шляхи до файлів
input_json = "students.json"

# Ім'я для пошуку (варіант 3)
search_name = "Марія"

# Зчитування json файлу
with open(input_json, "r", encoding="utf-8") as file:
    students = json.load(file)

# Пошук студентів з заданим іменем
formated_str = "{name:<30}{age:<4}{faculty:<8}"
for student in students:
    if student["name"] == search_name:
        print(formated_str.format(name=student["name"], age=student["age"], \
                                  faculty=student["faculty"]))