# Оголошуємо змінні з перетворенням типів
try:
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))

    print() # Відступ

    # Рахуємо додавання, віднімання та множення
    print(f"addition: {a+b:g} \nsubtraction: {a-b:g} \nmultiplication: {a*b:g}")

    # ділення з перевіркою на нуль
    if b == 0:
        print("division: Error (division by zero is not allowed)")
    else:
        print(f"division: {a/b:g}")

    print("-" * 20)

    # Програма для множення
    num1 = float(input("pershe: "))
    num2 = float(input("druge: "))
    print(f"Result: {num1 * num2:g}")

except ValueError:
    print("Error: Please enter valid numbers.")
except ZeroDivisionError:
    # Це на випадок, якщо щось проскочило повз if
    print("division: Error (Zero Division)")