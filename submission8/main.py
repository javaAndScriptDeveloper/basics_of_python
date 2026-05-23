class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def show_grades(self):
        print("Оцінки студента", self.name + ":")
        for grade in self.grades:
            print(grade)


name = input()
count = int(input())

student = Student(name)

for i in range(count):
    grade = int(input())
    student.add_grade(grade)

student.show_grades()