# Лабораторна робота 9: Регулярні вирази

import re

# Реалізуйте завдання тут

# Read input from stdin
text = input().strip()

# Replace all spaces with underscores using regex
result = re.sub(r' ', '_', text)

# Print the result
print(result)
