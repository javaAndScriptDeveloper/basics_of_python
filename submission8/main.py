# Лабораторна робота 8: Основи ООП

# Реалізуйте завдання тут
class Employee:
    def __init__(self, surname, name, age, position):
        self.surname = surname
        self.name = name
        self.age = age
        self.position = position
    def display(self):
        print(self.surname, self.name, self.age, self.position)

surname = input("Enter surname: ")
name = input("Enter name: ")
age = input("Enter age: ")
position = input("Enter position: ")
employee = Employee(surname, name, age, position)
employee.display()