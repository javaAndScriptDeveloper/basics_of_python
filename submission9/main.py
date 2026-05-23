import re

text = input()

words = re.findall(r'\b[А-ЯІЇЄҐA-Z][а-яіїєґa-zA-ZА-ЯІЇЄҐ]*\b', text)

if words:
    print(*words)
else:
    print("Не знайдено")