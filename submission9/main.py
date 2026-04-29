# Лабораторна робота 9: Регулярні вирази

# Реалізуйте завдання тут
import re

def find_capitalized_words(text):
    # [A-ZА-ЯІЇЄҐ] - велика літера
    # [a-zA-Zа-яА-ЯіїєґІЇЄҐ]* - решта літер слова
    pattern = r'\b[A-ZА-ЯІЇЄҐ][a-zA-Zа-яА-ЯіїєґІЇЄҐ]*\b'
    return re.findall(pattern, text)


def main():
    text = input("Введіть текст: ")

    words = find_capitalized_words(text)

    if words:
        print(f"\nЗнайдено {len(words)} слів з великої літери:")
        for word in words:
            print(f"{word}")
    else:
        print("\nСлів з великої літери не знайдено.")


if __name__ == "__main__":
    main()