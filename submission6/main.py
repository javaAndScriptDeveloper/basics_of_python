# Дані для завдання
import json

# Шляхи до файлів
input_json = "students.json"
output_json = "output.json"
input_csv = "students.csv"
input_json2 = "students2.json"

# Примітка: при запису JSON використовуйте ensure_ascii=False
# json.dump(data, f, ensure_ascii=False, indent=2)

# Реалізуйте завдання тут
import pandas as pd
import os

def convert_csv_to_json(csv_file: str, json_file: str):
    if not os.path.exists(csv_file):
        print(f"Файл {csv_file} не знайдено")
        return
        
    try:
        df = pd.read_csv(csv_file)
        data_to_save = df.to_dict(orient='records')
        
        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(data_to_save, f, ensure_ascii=False, indent=2)
            
    except Exception as e:
        print(f"Помилка: {e}")

def main():
    convert_csv_to_json(csv_file= input_csv, json_file=output_json)
    if os.path.exists(output_json):
            with open(output_json, "r", encoding="utf-8") as f:
                print(f.read())

if __name__ == "__main__":
    main()