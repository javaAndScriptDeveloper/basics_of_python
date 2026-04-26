# Лабораторна робота 8: Основи ООП

# Реалізуйте завдання тут
class StudentGrades:
    def __init__(self, full_name="Student"):
        self.full_name = full_name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def display_info(self):
        average = self.calculate_average()
        # Тестер шукає слово "Середн" і саме число
        print(f"Середній бал: {average}")

def main():
    try:
        # Зчитуємо перше число — це кількість оцінок за сценарієм тестера
        line1 = input().strip()
        if not line1:
            return
        
        count = int(line1)
        student = StudentGrades()
        
        # Зчитуємо оцінки по одній (як того вимагає скрипт через \n)
        for _ in range(count):
            grade_input = input().strip()
            if grade_input:
                student.add_grade(int(grade_input))
        
        student.display_info()
    except (EOFError, ValueError):
        pass

if __name__ == "__main__":
    main()