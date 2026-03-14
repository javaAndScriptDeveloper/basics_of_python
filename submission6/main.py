import json
import csv
import pandas as pd
import os


def create_initial_files():

    initial_students = [
        {"name": "Катя", "age": 20, "faculty": "Економіка"},
        {"name": "Марія", "age": 19, "faculty": "Економіка"},
        {"name": "Ліза", "age": 21, "faculty": "Мехатроніка"},
        {"name": "Мари", "age": 20, "faculty": "Маркетинг"},
        {"name": "Даша", "age": 18, "faculty": "Логістика"},
        {"name": "Діана", "age": 18, "faculty": "Архітектура"}
    ]

    with open("students.json", "w", encoding="utf-8") as f:
        json.dump(initial_students, f, ensure_ascii=False, indent=2)

    with open("students.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age", "faculty"])
        writer.writeheader()
        writer.writerows(initial_students)

    df = pd.DataFrame(initial_students)
    df.to_excel("students.xlsx", index=False)

    print("Початкові файли створено успішно\n")


def task_json():

    with open("students.json", "r", encoding="utf-8") as f:
        students = json.load(f)

    students.append({"name": "Анна", "age": 22, "faculty": "Інформатика"})
    students[0]["faculty"] = "ФТІ"

    students = [s for s in students if s["name"] != "Марія"]

    with open("students_updated.json", "w", encoding="utf-8") as f:
        json.dump(students, f, ensure_ascii=False, indent=2)

    print("Дані JSON оброблено та збережено y students_updated.json\n")


def task_csv():

    students_csv = []

    with open("students.csv", "r", encoding="utf-8") as f:

        reader = csv.DictReader(f)

        for row in reader:
            row["age"] = int(row["age"])
            students_csv.append(row)

    students_csv.append({"name": "Саша", "age": 22, "faculty": "Право"})

    with open("students_updated.csv", "w", newline="", encoding="utf-8") as f:
        fieldnames = ["name", "age", "faculty"]

        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students_csv)

    print("Дані CSV оброблено та збережено у students_updated.csv\n")


def task_excel():

    df = pd.read_excel("students.xlsx")

    df_filtered = df[df["age"] > 19]
    df_sorted = df_filtered.sort_values(by="age", ascending=True)

    df_sorted.to_excel("students_processed.xlsx", index=False)
    
    print("Дані Excel відфільтровано та збережено у students_processed.xlsx\n")


def individual_task_2(new_name, new_age, new_faculty):

    try:
        with open("students.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        new_entry = {"name": new_name, "age": new_age, "faculty": new_faculty}
        data.append(new_entry)

        with open("students.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        with open("output.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print(f"Студент {new_name} успішно доданий до students.json та output.json\n")

    except Exception as e:
        print(f"Виникла помилка: {e}")


create_initial_files()

task_json()
task_csv()
task_excel()

individual_task_2("Сергій", 24, "ФМ")

