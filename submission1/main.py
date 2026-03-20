number = float(input("Введіть перше число:"))
number1 = float(input("Введіть друге число:"))
res1 = number1 + number
res2 = number - number1
res3 = number * number1
if number1 != 0:
    res4 = number / number1
else:
    res4 = "Помилка при діленні на нуль"
print(
    f"Результати виконання простих арифметичних дій над числами: сумма - {res1}, різниця - {res2}, множення - {res3}, ділення - {res4}")

if number % 2 == 0:
    print("Число парне")
else:
    print("число непарне")
# Implement task here
