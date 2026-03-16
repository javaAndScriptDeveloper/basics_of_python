#Побудувати таблицю множення для заданого числа

# Введення числа з клавіатури
number = float(input("Введіть число: "))

print(f"Таблиця множення для числа {number}:")

# Цикл від 1 до 10
for i in range(1, 11):
    result = number * i
    print(f"{number} * {i} = {result}")

