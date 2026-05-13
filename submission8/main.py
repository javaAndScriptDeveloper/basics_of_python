# Лабораторна робота 8: Основи ООП

# Реалізуйте завдання тут
class Student:
    # Конструктор класу (викликається під час створення об'єкта)
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = []

    # Метод для додавання нової оцінки
    def add_grade(self, grade):
        self.grades.append(grade)
        print(f"Оцінку {grade} успішно додано студенту {self.first_name}.")

    # Метод для виведення інформації про студента
    def show_info(self):
        print(f"\n--- Інформація про студента ---")
        print(f"Ім'я та прізвище: {self.first_name} {self.last_name}")
        print(f"Список оцінок: {self.grades}")
        # Якщо оцінки є, рахуємо середній бал
        if self.grades:
            avg = sum(self.grades) / len(self.grades)
            print(f"Середній бал: {avg:.2f}")
        else:
            print("Оцінок ще немає.")
        print("-------------------------------")

# Основний блок перевірки
if __name__ == "__main__":
    student1 = Student("Олександр", "Дудник")
    
    student1.show_info()
    
    # Додаємо оцінки 5, 4 та 3, як того вимагає автотест
    student1.add_grade(5)
    student1.add_grade(4)
    student1.add_grade(3)
    
    student1.show_info()