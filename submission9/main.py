import re

user_str = input("Введіть рядок для видалення зайвих пробілів: ")
result = re.sub(r'\s+', ' ', user_str)
print(result)