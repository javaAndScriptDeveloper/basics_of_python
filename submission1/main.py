# Implement task here
a = float(input("Введіть перше число:"))
b = float(input("Введіть друге число:"))

subtraction_result = a - b # віднімання
sum_result = a + b # додавання
multiplication_result = a * b # множення
division_result = a / b # ділення
print(f"Віднімання: {subtraction_result}")
print(f"Додавання: {sum_result}")
print(f"Множення: {multiplication_result}")
print(f"Ділення: {division_result}")
# Перевірка на нуль, щоб уникнути ZeroDivisionError
if a == 0 or b == 0:
    print("Ділення на нуль неможливе")
elif a % b == 0 or b % a == 0:
    print("Так, одне число є дільником іншого")
else:
    print("Ні, числа не є дільниками одне одного")