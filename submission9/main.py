# Лабораторна робота 9: Регулярні вирази

# Реалізуйте завдання тут
import re

text = input()

# замінюємо один або більше пробілів на один пробіл
cleaned = re.sub(r'\s+', ' ', text).strip()

print(cleaned)