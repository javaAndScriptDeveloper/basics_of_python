# Дані для завдання
import json

# Шляхи до файлів
input_json = "students.json"
output_json = "output.json"

# Ім'я для пошуку (варіант 3)
search_name = "Марія"


# Примітка: при запису JSON використовуйте ensure_ascii=False
# json.dump(data, f, ensure_ascii=False, indent=2)

# Реалізуйте завдання тут
import json
import sys

input_json = 'students.json'
output_json = 'output.json'

# single source for search name; can pass override as first CLI arg
search_name = sys.argv[1] if len(sys.argv) > 1 else "Марія"

def extract_students(data):
    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        for key in ("students", "Students", "data", "items"):
            if key in data and isinstance(data[key], list):
                return data[key]
        values = [v for v in data.values() if isinstance(v, dict)]
        if values:
            return values
    return []

def student_name_value(student):
    for k in ("name", "Name", "ім'я", "Ім'я", "firstname", "first_name", "firstName"):
        if k in student:
            return student[k]
    for v in student.values():
        if isinstance(v, str):
            return v
    return None

def find_students_by_name(students, target):
    target_norm = target.strip().casefold()
    matches = []
    for s in students:
        if not isinstance(s, dict):
            continue
        name_val = student_name_value(s)
        if not isinstance(name_val, str):
            continue
        if name_val.strip().casefold() == target_norm:
            matches.append(s)
    return matches

def main():
    try:
        with open(input_json, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Input file ` {input_json} ` not found.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Failed to parse ` {input_json} `: {e}")
        sys.exit(1)

    students = extract_students(data)
    matches = find_students_by_name(students, search_name)

    if matches:
        print(json.dumps(matches if len(matches) > 1 else matches[0], ensure_ascii=False, indent=2))
        with open(output_json, "w", encoding="utf-8") as out_f:
            json.dump(matches if len(matches) > 1 else matches[0], out_f, ensure_ascii=False, indent=2)
    else:
        print(f"No student named `{search_name}` found in ` {input_json} `.")
        with open(output_json, "w", encoding="utf-8") as out_f:
            json.dump([], out_f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
