# Лабораторна робота 8: Основи ООП

# Реалізуйте завдання тут
class StudentGrades:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        """Додає оцінку до списку оцінок студента."""
        if 0 <= grade <= 100:
            self.grades.append(grade)
            print(f"Оцінку {grade} додано.")
        else:
            print(f"Помилка: оцінка {grade} поза допустимим діапазоном.")

    def average(self):
        """Обчислює та повертає середній бал студента."""
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def show_info(self):
        """Виводить інформацію про студента та його оцінки."""
        print(f"\nСтудент: {self.name}")
        if self.grades:
            print(f"Оцінки: {self.grades}")
            print(f"Середній бал: {self.average():.2f}")
        else:
            print("Оцінок ще немає.")


def main():
    name = input("Введіть ім'я студента: ")
    student = StudentGrades(name)

    while True:
        raw = input("Введіть оцінку (або 'стоп' для завершення): ")
        if raw.lower() == "стоп":
            break
        try:
            grade = float(raw)
            student.add_grade(grade)
        except ValueError:
            print("Помилка: введіть числове значення або 'стоп'.")

    student.show_info()


if __name__ == "__main__":
    main()