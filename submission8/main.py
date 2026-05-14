import sys

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

def solve():
    try:
        input_data = sys.stdin.read().split()
        if len(input_data) < 2:
            return

        w = float(input_data[0])
        h = float(input_data[1])

        # Створюємо об'єкт класу
        rect = Rectangle(w, h)

        print(f"Площа: {rect.get_area()}")
        print(f"Периметр: {rect.get_perimeter()}")

    except EOFError:
        pass
    except ValueError:
        pass

if __name__ == "__main__":
    solve()