import json


def load_json_file(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except UnicodeDecodeError:
        with open(path, "r", encoding="cp1251") as file:
            return json.load(file)


students = load_json_file("students.json")

for student in students:
    if student["name"] == "Іван":
        student["faculty"] = "КН"

with open("output.json", "w", encoding="utf-8") as file:
    json.dump(students, file, ensure_ascii=False, indent=4)