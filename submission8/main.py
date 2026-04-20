import sys

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.length + self.width)

def main():
    try:
        # Зчитуємо дані (довжину та ширину), які подає скрипт перевірки
        input_data = sys.stdin.read().split()
        if len(input_data) < 2:
            return

        length = float(input_data[0])
        width = float(input_data[1])

        # Створюємо об'єкт класу
        rect = Rectangle(length, width)

        # Виводимо результати так, як їх очікує регулярний вираз у тесті
        area = rect.get_area()
        perimeter = rect.get_perimeter()

        # Форматуємо вивід, щоб він містив потрібні цифри
        print(f"Площа: {area}")
        print(f"Периметр: {perimeter}")

    except ValueError:
        pass

if __name__ == "__main__":
    main()