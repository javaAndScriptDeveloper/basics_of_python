# Лабораторна робота 8: Основи ООП
import datetime


class Student:
    def __init__(self, birth_year):
        self.birth_year = birth_year

    def calculate_age(self):
        #Метод обчислення віку на основі поточної дати
        current_year = datetime.date.today().year
        return current_year - self.birth_year

try:
    #Зчитування
    user_input = input("Введіть рік народження: ")
    year = int(user_input)

    #Створення об'єкту класу
    student_instance = Student(year)

    #Виклик та вивід результату
    age = student_instance.calculate_age()

    print(f"Вік: {age}")

except ValueError:
    print("Помилка: необхідно ввести ціле число (рік).")