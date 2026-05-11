# Лабораторна робота 9: Регулярні вирази
import re
import sys

def remove_spaces(text):
    #Регулярний вираз для заміни будь-якої послідовності пробілів на один пробіл.
    # \s+ знаходить один або більше пробілів, табуляцій або переносів
    pattern = r'\s+'
    cleaned_text = re.sub(pattern, ' ', text)
    return cleaned_text.strip()

def main():
    try:
        # Зчитуємо ввід
        input_data = sys.stdin.read()

        if not input_data:
            return

        result = remove_spaces(input_data)
        print(result)

    except Exception as e:
        print(f"Виникла помилка: {e}")


if __name__ == "__main__":
    main()