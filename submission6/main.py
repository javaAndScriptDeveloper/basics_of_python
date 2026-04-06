import json

with open("students.json", "r", encoding="utf-8") as f:
    students = json.load(f) #

students = [student for student in students if student["name"] != "Петро"] #Видалення Петра

with open("output.json", "w", encoding="utf-8") as f:
    json.dump(students, f, ensure_ascii=False, indent=2)

print("Студента 'Петро' видалено.")