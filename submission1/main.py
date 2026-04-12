def main():
    try:
        a = int(input())
        b = int(input())

        print(f"Сума: {a + b}")
        print(f"Різниця: {a - b}")
        print(f"Добуток: {a * b}")

        if b != 0:
            print(f"Частка: {a / b}")
        else:
            print("Частка: Ділення на нуль неможливе")
            
        if b != 0 and a % b == 0:
            print("Значення b є дільником значення a")
        elif a != 0 and b % a == 0:
            print("Значення a є дільником значення b")
        else:
            print("Обидва числа не є дільником один одного")

    except ValueError:
        print("Помилка: Введено не ціле число!")

if __name__ == "__main__":
    main()