# 1. Реалізація функції для знаходження найбільшого з трьох чисел
def find_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


def main():
    # 2. Викликаємо функцію для трьох наборів чисел,

    # Набір 1 (результат 17)
    res1 = find_max(17, 5, 12)

    # Набір 2 (результат 10)
    res2 = find_max(3, 10, 8)

    # Набір 3 (результат 42)
    res3 = find_max(20, 15, 42)

    # 3. Виведення результатів
    print(res1)
    print(res2)
    print(res3)


if __name__ == "__main__":
    main()