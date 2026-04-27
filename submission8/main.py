from datetime import datetime

class Student:
    def __init__(self, birth_year):
        self.birth_year = birth_year

    def get_age(self):
        current_year = datetime.now().year
        return current_year - self.birth_year


birth_year = int(input())
student = Student(birth_year)

print("Вік студента:", student.get_age(), "років")