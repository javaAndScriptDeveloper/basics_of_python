num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))

sum_res = num1 + num2
diff_res = num1 - num2
div_res = num1 / num2 if num2 != 0 else "Ділення на нуль неможливе!"

mult_res = num1 * num2

print("\n Результати обчислень")
print(f"Сума: {sum_res}")
print(f"Різниця: {diff_res}")
print(f"Частка: {div_res}")
print(f"Добуток чисел {num1} та {num2} дорівнює: {mult_res}")
