# Implement task here
# 1. Введення початкових даних
try:
    number = int(input("Введіть число для побудови таблиці множення: "))

    print(f"\nТаблиця множення для числа {number}:")
    print("-" * 20)

    # 2. Виконання розрахунків та (3) виведення результатів
    # Використовуємо цикл від 1 до 10 включно
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")

    print("-" * 20)

except ValueError:
    print("Помилка: будь ласка, введіть ціле число.")