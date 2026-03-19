def find_max_of_three(a, b, c):
 
    result = max(a, b, c)
    return result

def main():
    print("--- Програма для знаходження найбільшого з трьох чисел ---")
    
    try:
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))
        num3 = float(input("Введіть третє число: "))
        
        max_value = find_max_of_three(num1, num2, num3)
        
        print(f"Найбільше число - {max_value}")
    except ValueError:
        print("Помилка: введіть коректні числа.")

if __name__ == "__main__":
    main()