# Зчитуємо два числа з клавіатури
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))

# Виконуємо арифметичні операції
sum_result = a + b
diff_result = a - b
mul_result = a * b

# Ділення з перевіркою на нуль
if b != 0:
    div_result = a / b
else:
    div_result = None

# Виводимо результати
print(f"\nДодавання:    {a} + {b} = {sum_result}")
print(f"Віднімання:   {a} - {b} = {diff_result}")
print(f"Множення:     {a} * {b} = {mul_result}")

if div_result is not None:
    print(f"Ділення:      {a} / {b} = {div_result}")
else:
    print("Ділення:      ділення на нуль неможливе")

# Індивідуальне завдання: множення двох введених чисел
print(f"\nРезультат множення: {a} * {b} = {mul_result}")
# Implement task here
