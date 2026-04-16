# Лабораторна робота 9: Регулярні вирази

# Реалізуйте завдання тут
import sys
import re

def main():
    # Зчитуємо вхідний рядок зі стандартного вводу
    input_text = sys.stdin.read().strip()
    
    if not input_text:
        return

    result = re.sub(r'\s+', '_', input_text)
    
    # Виводимо результат
    print(result)

if __name__ == "__main__":
    main()