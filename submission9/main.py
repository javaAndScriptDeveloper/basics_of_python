# Лабораторна робота 9: Регулярні вирази

# Реалізуйте завдання тут
import re
text = input()
emails = re.findall(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', text)
if emails:
    print(*emails)
else:
    print("Не знайдено")