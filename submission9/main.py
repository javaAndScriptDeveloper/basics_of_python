# Лабораторна робота 9: Регулярні вирази

# Реалізуйте завдання тут
import re
import sys

def process_text(input_string):
    pattern = r'\d'
    result = re.sub(pattern, '#', input_string)
    return result

def main():
    input_data = sys.stdin.read().strip()

    if input_data:
        final_result = process_text(input_data)
        print(final_result)

    else:
        pass
if __name__ == '__main__':
    main()
