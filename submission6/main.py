import json
import csv
import pandas as pd

input_json = "students.json"
output_json = "output.json"
input_csv = "students.csv"
input_json2 = "students2.json"

new_student = {"name": "Сергій", "age": 24, "faculty": "ФМ"}

def create_initial_files():

    initial_students = [
        {"name": "Катя", "age": 20, "faculty": "Економіка"},
        {"name": "Марія", "age": 19, "faculty": "Економіка"},
        {"name": "Ліза", "age": 21, "faculty": "Мехатроніка"},
        {"name": "Мари", "age": 20, "faculty": "Маркетинг"},
        {"name": "Даша", "age": 18, "faculty": "Логістика"},
        {"name": "Діана", "age": 18, "faculty": "Архітектура"}
    ]
    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(initial_students, f, ensure_ascii=False, indent=2)
    with open(input_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age", "faculty"])
        writer.writeheader()
        writer.writerows(initial_students)

    df = pd.DataFrame(initial_students)
    df.to_excel("students.xlsx", index=False)
    


def task_json():
    with open(output_json, "r", encoding="utf-8") as f:
        students = json.load(f)

    students.append({"name": "Анна", "age": 22, "faculty": "Інформатика"})
    students[0]["faculty"] = "ФТІ"

    students = [s for s in students if s["name"] != "Марія"]
    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(students, f, ensure_ascii=False, indent=2)



def task_csv():

    students_csv = []
    with open(input_csv, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            row["age"] = int(row["age"])
            students_csv.append(row)

    students_csv.append({"name": "Саша", "age": 22, "faculty": "Право"})

    with open("students_updated.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age", "faculty"])
        writer.writeheader()
        writer.writerows(students_csv)
    
def task_excel():

    df = pd.read_excel("students.xlsx")

    df_filtered = df[df["age"] > 19]
    df_sorted = df_filtered.sort_values(by="age", ascending=True)

    df_sorted.to_excel("students_processed.xlsx", index=False)

def individual_task_2():
    with open(output_json, "r", encoding="utf-8") as f:
        data = json.load(f)
    data.append(new_student)

    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


create_initial_files()

task_json()
task_csv()
task_excel()

individual_task_2()
