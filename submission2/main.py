try:
    number = float(input("Введіть число для таблиці множення: "))
    if number > 0:
        print("Число є додатнім")
    elif number < 0:
        print("Працюємо з від’ємним числом:")
    else:
        print(f"Таблиця множення для {number}:")

    print(f"{number} * 1 = {number * 1}")
    print(f"{number} * 2 = {number * 2}")
    print(f"{number} * 3 = {number * 3}")
    print(f"{number} * 4 = {number * 4}")
    print(f"{number} * 5 = {number * 5}")
    print(f"{number} * 6 = {number * 6}")
    print(f"{number} * 7 = {number * 7}")
    print(f"{number} * 8 = {number * 8}")
    print(f"{number} * 9 = {number * 9}")
    print(f"{number} * 10 = {number * 10}")

except ValueError:
    print("Помилка: введіть коректне число.")
except EOFError:
    pass