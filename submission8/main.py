# Лабораторна робота 8: Основи ООП

# Реалізуйте завдання тут
class Student:
    def __init__(self, first_name, last_name):
        """Конструктор: ініціалізація імені та прізвища"""
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        """Повертає повне ім'я студента"""
        return f"{self.first_name} {self.last_name}"

    def display_info(self):
        """Виводить інформацію про студента"""
        print(f"Студент: {self.get_full_name()}")


# Введення даних
first_name = input("Введіть ім'я студента: ")
last_name = input("Введіть прізвище студента: ")

# Створення об'єкта
student = Student(first_name, last_name)

# Виведення результату
student.display_info()