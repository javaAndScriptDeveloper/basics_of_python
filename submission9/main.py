# Лабораторна робота 9: Регулярні вирази

# Реалізуйте завдання тут
import re

def replace_digits(text):
    """Замінює всі цифри у рядку на символ #"""
    result = re.sub(r'\d', '#', text)
    return result

# Введення даних
text = input("Введіть рядок: ")

# Обробка
result = replace_digits(text)

# Виведення результату
print(f"Оригінал : {text}")
print(f"Результат: {result}")