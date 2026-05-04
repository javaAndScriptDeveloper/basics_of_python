import csv
import json
import os


input_csv = "students.csv"
output_json = "output.json"

def main():

    if not os.path.exists(input_csv):
        with open(input_csv, mode="w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["name", "age", "faculty"])
            writer.writerow(["Олександр", "20", "ФІОТ"])
            writer.writerow(["Марія", "21", "КН"])

    try:
        data = []
        with open(input_csv, mode="r", encoding="utf-8") as csvf:
            reader = csv.DictReader(csvf)
            for row in reader:
                data.append(row)
        with open(output_json, mode="w", encoding="utf-8") as jsonf:
            json.dump(data, jsonf, ensure_ascii=False, indent=2)

        print(f"Успіх: Дані з {input_csv} успішно конвертовано та збережено у {output_json}!")

    except Exception as e:
        print(f"Сталася неочікувана помилка: {e}")

if __name__ == "__main__":
    main()