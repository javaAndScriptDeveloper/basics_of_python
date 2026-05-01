# Лабораторна робота 9: Регулярні вирази

# Реалізуйте завдання тут
import re
def clean(text):
    text = re.sub(r'\d', '#', text)
    return text
inp=input("Введіть текст для очистки від #")
if not inp.strip():
        print("Помилка: Ви нічого не ввели!")
else:
    print(clean(inp))
