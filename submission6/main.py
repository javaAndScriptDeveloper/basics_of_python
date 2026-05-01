import csv
import json
import os

input_csv = "students.csv"
output_json = "output.json"

data_list = []

if os.path.exists(input_csv):
    try:
        with open(input_csv, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data_list.append(row)
    except Exception:
        pass
else:
    data_list = [
        {"name": "Олена", "age": 20, "faculty": "ФІТ"},
        {"name": "Іван", "age": 21, "faculty": "ФІТ"},
        {"name": "Марія", "age": 19, "faculty": "Економіка"}
    ]

with open(output_json, 'w', encoding='utf-8') as json_file:
    json.dump(data_list, json_file, ensure_ascii=False, indent=2)