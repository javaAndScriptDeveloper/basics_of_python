# Реалізуйте завдання тут
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

input_file = "input.txt"
output_file = "output.txt"

try:
    with open(input_file, 'r', encoding='utf-8') as infile:
        data = infile.read()

    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write(data)

    print(f"перемога! Дані скопійовано з {os.path.basename(input_file)} у {os.path.basename(output_file)}")


except FileNotFoundError:
    print(f"Помилка: Файл {input_file} не знайдено.")
except Exception as e:
    print(f"Сталася непередбачувана помилка: {e}")