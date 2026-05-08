import datetime


class Student:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth

    def get_age(self):
        today = datetime.date.today()
        age = today.year - self.date_of_birth
        return f'Вік: {age}.'

student1 = Student('', 2000)
print(student1.get_age())
student2 = Student('', 1990)
print(student2.get_age())
