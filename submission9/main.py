# Лабораторна робота 9: Регулярні вирази

# Реалізуйте завдання тут
import re

text = input()
pattern = r'(\d{2})-(\d{2})-(\d{4})'
result = re.sub(pattern, r'\3-\2-\1', text)
print(result)
