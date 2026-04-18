# Лабораторна робота 8: Основи ООП

# Реалізуйте завдання тут
# 8.Написати клас, який обчислює площу та периметр прямокутника

# Оголошення класу Rectangle
class Rectangle:
    # Конструктор класу (метод ініціалізації об'єкта)
    def __init__(self, width, height):
        self.width = width                      #ширина
        self.height = height                    #висота

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    # Метод для виведення інформації про прямокутник
    def show_info(self):
        print(f"Площа прямокутника: {self.get_area()}")
        print(f"Периметр прямокутника: {self.get_perimeter()}")


try:
    width = float(input("Введіть ширину: "))
    height = float(input("Введіть висоту: "))

    # Створюємо об'єкт з отриманими даними
    rectangle1 = Rectangle(width, height)

    # Виводимо інформацію
    rectangle1.show_info()
except EOFError:
    pass

