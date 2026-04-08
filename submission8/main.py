# Лабораторна робота 8: Основи ООП

# Реалізуйте завдання тут
class GradeBook:
    def __init__(self):
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)


count = int(input())
book = GradeBook()

for _ in range(count):
    book.add_grade(int(input()))

print(f"Середній бал: {book.average():.1f}")