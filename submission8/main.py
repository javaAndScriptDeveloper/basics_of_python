# Лабораторна робота 8: Основи ООП

# Реалізуйте завдання тут

class GradeAverage:
    """Class for calculating the average value of a group of grades."""

    def __init__(self):
        self.grades = []

    def add_grade(self, grade):
        """Add a grade to the list."""
        self.grades.append(grade)

    def calculate_average(self):
        """Calculate and return the average of grades."""
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def display_average(self):
        """Display the average with a label."""
        avg = self.calculate_average()
        # Round to nearest integer
        rounded_avg = round(avg)
        print(f"Середнє значення: {rounded_avg}")

# Read grades from stdin
grade_avg = GradeAverage()

while True:
    try:
        grade_input = input().strip()
        if grade_input:
            grade = int(grade_input)
            grade_avg.add_grade(grade)
    except EOFError:
        break
    except ValueError:
        pass

# Display the average
grade_avg.display_average()
