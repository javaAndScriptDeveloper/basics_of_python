import json


def main():
    courses = [
        {
            "id": 1,
            "title": "Об'єктно-орієнтоване програмування",
            "teacher": "Барбарук В.М."
        },
        {
            "id": 2,
            "title": "Бази даних",
            "teacher": "Ковальчук О.П."
        },
        {
            "id": 3,
            "title": "Алгоритми та структури даних",
            "teacher": "Сидоренко І.В."
        }
    ]

    filename = "output.json"

    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(courses, file, ensure_ascii=False, indent=4)

        print("Файл успішно створено з необхідними курсами.")

    except Exception:
        pass


if __name__ == "__main__":
    main()