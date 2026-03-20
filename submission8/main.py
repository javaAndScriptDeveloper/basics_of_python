class CalcGrades:
    def __init__(self):
        self.__grades = []

    def add_grade(self, grade):
        self.__grades.append(grade)

    def avg_grade(self):
        return sum(self.__grades) / len(self.__grades)


n = int(input())
calc = CalcGrades()

for _ in range(n):
    calc.add_grade(int(input()))

avg = calc.avg_grade()
print(f"Середнє: {avg}")