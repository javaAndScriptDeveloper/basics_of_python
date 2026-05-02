# Лабораторна робота 9: Регулярні вирази

# Реалізуйте завдання тут
import sys
import re

input_text = sys.stdin.read().strip()
if not input_text:
    try:
        input_text = input().strip()
    except EOFError:
        pass

pattern = r"^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$"

if re.match(pattern, input_text):
    print("Коректно")
else:
    print("Некоректно")