# Лабораторна робота 8: Основи ООП

# Реалізуйте завдання тут
class StudentGrades:
    """Клас для зберігання оцінок студента та розрахунку середнього бала."""
    
    def __init__(self, full_name):
        """Конструктор класу."""
        self.full_name = full_name
        self.grades = []

    def add_grades(self, grades_list):
        """Метод для додавання списку оцінок."""
        self.grades.extend(grades_list)

    def calculate_average(self):
        """Метод для розрахунку середнього значення оцінок."""
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def display_info(self):
        """Метод для виведення результатів."""
        average = self.calculate_average()
        print(f"\n--- Результат ---")
        print(f"Студент: {self.full_name}")
        print(f"Оцінки: {self.grades}")
        print(f"Середній бал: {average:.2f}")


def main():
    print("Введення початкових даних")
    name = input("Введіть прізвище та ім'я студента: ")
    
    # Створення об'єкта класу
    student = StudentGrades(name)
    
    try:
        raw_grades = input("Введіть оцінки через пробіл: ")
        # Перетворення введеного рядка у список цілих чисел
        grades_list = [int(g) for g in raw_grades.split()]
        
        # Використання методів об'єкта
        student.add_grades(grades_list)
        student.display_info()
        
    except ValueError:
        print("Помилка: будь ласка, вводьте лише цілі числа для оцінок.")

if __name__ == "__main__":
    main()