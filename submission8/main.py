# Лабораторна робота 8: Основи ООП

# Реалізуйте завдання тут
from datetime import date

class Student:
    def __init__(self, birth_year):
        self.birth_year = birth_year

    # Обчислює вік студента на основі поточного року
    def get_age(self):
        return date.today().year - self.birth_year

# Вводимо рік народження
birth_year = int(input("Введіть рік народження: "))

student = Student(birth_year)

# Виводимо результат
print(f"Вік: {student.get_age()} років")
