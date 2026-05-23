try:
    number = int(input())

    if number < 0:
        raise ValueError("Від'ємне число")

    print("Додатне число:", number)

except ValueError:
    print("Помилка: введене число є від'ємним або некоректним")