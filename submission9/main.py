# Лабораторна робота 9: Регулярні вирази

# Реалізуйте завдання тут
import re


def main():
    print("*** Програма для очищення тексту від небажаних символів ***")
    input_text = input("Введіть текст: ")
    output_text = make_clean_text(input_text)
    print(output_text)


def make_clean_text(text):
    """Видаляє всі символи, крім літер, цифр та пробілів."""
    pattern = r"[^A-Za-z0-9 ]"
    clean_text = re.sub(pattern, "", text)
    return clean_text


if __name__ == "__main__":
    main()
