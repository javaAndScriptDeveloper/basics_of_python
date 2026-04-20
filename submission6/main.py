import json
import os

def main():
    courses = [
        {
            "name": "програмування на Python",
            "instructor": "Барбарук В.М.",
            "credits": 5
        },
        {
            "name": "Бази даних",
            "instructor": "Сидоренко А.П.",
            "credits": 3
        },
        {
            "name": "Алгоритми та структури даних",
            "instructor": "Петренко О.І.",
            "credits": 4
        }
    ]

    output_file = "output.json"
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(courses, f, ensure_ascii=False, indent=4)
        print(f"Індивідуальне завдання: дані збережено в {output_file}")
    except Exception as e:
        print(f"Помилка запису JSON: {e}")


  
    input_file = "students.json"
    

    if os.path.exists(input_file):
        try:
            with open(input_file, "r", encoding="utf-8") as f:
                students_data = json.load(f)
                print("\nЗагальне завдання (зчитано з файлу):")
                for student in students_data:
                    print(f"- Студент: {student['name']}, Факультет: {student['faculty']}")
        except Exception as e:
            print(f"Помилка читання JSON: {e}")
    else:

        print(f"\nℹФайл {input_file} не знайдено (пропускаємо загальне завдання для тесту).")

if __name__ == "__main__":
    main()