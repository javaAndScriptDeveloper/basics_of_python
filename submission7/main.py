# Реалізуйте завдання тут
try:
    user_input = input("Введіть числа через пробіл: ").strip()

    if not user_input:
        raise ValueError("Список порожній!")

    numbers = list(map(float, user_input.split()))

    print("Ви ввели список чисел:", numbers)

except ValueError as e:
    print("Помилка:", e)