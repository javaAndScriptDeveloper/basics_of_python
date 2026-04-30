# Лабораторна робота 8: Основи ООП

# Реалізуйте завдання тут
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    def show_info(self):
        print("\nІнформація про студента:")
        print("Ім'я:", self.name)
        print("Оцінки:", self.grades)
        print("Середній бал:", round(self.average(), 2))

name = input("Введіть ім'я студента: ")
student = Student(name)

n = int(input("Кількість оцінок: "))

for i in range(n):
    grade = float(input(f"Оцінка {i + 1}: "))
    student.add_grade(grade)

student.show_info()
