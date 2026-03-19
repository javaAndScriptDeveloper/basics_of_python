# Дані для завдання

# Шлях до вхідного файлу
input_file = "input.txt"

# Новий вміст для перезапису (варіант 10)
new_content = "Файл перезаписано"

# Реалізуйте завдання тут

import os.path

file = "input.txt"
if os.path.exists(file):
    with open(file, "w") as f:
        f.write("Файл перезаписано")
        print("File is rewrited")
else:
    print("file not exist")
