# Лабораторна робота 9: Регулярні вирази

# Реалізуйте завдання тут
import re

text = input()

emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)

if emails:
    for email in emails:
        print(email)
else:
    print("Не знайдено")