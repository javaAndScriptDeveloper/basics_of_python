# Дані для завдання

# Словник для перевірки (варіант 6)
data = {"name": "Олена", "age": 20, "faculty": "КН"}

# Файл для запису помилок (варіант 8)
error_file = "error.log"

# Файл для зчитування (варіанти 5, 9)
input_file = "input.txt"

# Формат даних у файлі (варіант 9): "ім'я:вік" у кожному рядку

# Реалізуйте завдання тут
def main():
    key = input("Введіть ключ для перевірки: ")
    result = check_key_in_dict(key, data)
    print(result)


def check_key_in_dict(key, dictionary):
    try:
        value = dictionary[key]
        return value
    except KeyError:
        return "Ключ не знайдено"


if __name__ == "__main__":
    main()
