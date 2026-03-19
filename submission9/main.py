# Лабораторна робота 9: Регулярні вирази

import re

try:

    user_input = input()
    
    if not user_input:
        raise ValueError("Помилка! Рядок порожній")
    
    cleaned_text = re.sub(r'\s+', ' ', user_input)
    
   
    print(cleaned_text.strip())

except ValueError as err:
    print(err)
except EOFError:
    print("Помилка! Немає вхідних даних")