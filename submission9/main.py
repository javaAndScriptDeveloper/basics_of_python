import re

pattern = r'\b[A-ZА-ЯІЇЄҐ]\w*'

text_1 = "Hello everyone! Welcome to Python programming. It is a Great experience!"
text_2 = "це текст у якому немає жодної великої літери."

print("--- Лабораторна робота №9 (Варіант 4) ---")
print(f"Знайдені слова (Текст 1): {re.findall(pattern, text_1)}")
print(f"Знайдені слова (Текст 2): {re.findall(pattern, text_2)}")
