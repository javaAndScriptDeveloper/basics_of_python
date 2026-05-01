# Лабораторна робота 8: Основи ООП

# Реалізуйте завдання тут
class Student:
    def __init__(self, f_name, l_name):
        self.first_name = f_name
        self.last_name = l_name

    def get_name(self):
        return f"{self.first_name} {self.last_name}"

    def disp_info(self):
        print(f"Зареєстровано студента: {self.get_name()}")

f_name = input("Введіть ім'я студента: ").strip()
l_name = input("Введіть прізвище студента: ").strip()
if not f_name or not l_name:
    print("Помилка: Ім'я та прізвище не можуть бути порожніми!")
cur_student = Student(f_name, l_name)
print("\n--- Результат ---")
cur_student.disp_info()
