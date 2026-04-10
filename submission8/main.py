# Лабораторна робота 8: Основи ООП

# Реалізуйте завдання тут

import sys

class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def display_info(self):
        print(f"{self.first_name} {self.last_name}")

def main():
    input_data = sys.stdin.read().split()

    if len(input_data) >= 2:
        first_name = input_data[0]
        last_name = input_data[1]

        student = Student(first_name, last_name)

        student.display_info()

if __name__ == "__main__":
    main()