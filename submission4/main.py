import sys

def inches_to_cm(inches):
    """
    Функція приймає значення в дюймах і повертає сантиметри.
    """
    return inches * 2.54

def main():

    input_data = sys.stdin.read().split()
    for item in input_data:
        try:
            inches = float(item)
            cm = inches_to_cm(inches)
            print(cm)
        except ValueError:
            print(f"Помилка: '{item}' не є числом.")

if __name__ == "__main__":
    main()