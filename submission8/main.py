# Лабораторна робота 8: Основи ООП

# Реалізуйте завдання тут
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

l = float(input())
w = float(input())

rect = Rectangle(l, w)

area = rect.calculate_area()
perimeter = rect.calculate_perimeter()

print(f"Площа: {area}")
print(f"Периметр: {perimeter}")
