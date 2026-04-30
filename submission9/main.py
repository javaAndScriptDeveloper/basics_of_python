# Лабораторна робота 9: Регулярні вирази

# Реалізуйте завдання тут
import re

text=input()

pattern = r'\b[A-ZА-ЯІЇЄҐ][a-zа-яіїєґ]*\b'

result = re.findall(pattern, text)

print("Слова з великої літери:")
print(result)
