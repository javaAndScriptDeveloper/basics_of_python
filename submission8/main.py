class Student:
    def __init__(self, birth_year):
        self.birth_year = birth_year

    def calc_age(self):
        return 2026 - self.birth_year
    
birth_year = int(input())
student = Student(birth_year)
print(f"Вік {student.calc_age()} роки")