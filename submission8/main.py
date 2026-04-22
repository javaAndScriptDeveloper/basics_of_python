# Лабораторна робота №8
# Варіант 4
# Тема: Класи та об'єкти: основи об'єктно-орієнтованого програмування в Python.

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []  

    def add_grade(self, grade):
        self.grades.append(grade)

    def show_info(self):
        grades_str = ", ".join(map(str, self.grades))
        print(f"Студент: {self.name}")
        print(f"Оцінки: {grades_str}")

def main():
    name = input("Введіть ім'я студента: ")
    student = Student(name) 
    
    try:
        n = int(input("Введіть кількість оцінок: "))
        
        for i in range(n):
            grade = int(input(f"Введіть оцінку {i + 1}: "))
            student.add_grade(grade) 
            
    except ValueError:
        print("Помилка: потрібно вводити цілі числа.")
        
    student.show_info()

if __name__ == "__main__":
    main()