def find_max(a, b, c):
 
    result = max(a, b, c)
    return result

def main():
    try:
        num1 = float(input())
        num2 = float(input())
        num3 = float(input())
        
        max_value = find_max(num1, num2, num3)
        print(max_value) # Роботи люблять, коли виводиться ТІЛЬКИ число
    except ValueError:
        print("Помилка")

if __name__ == "__main__":
    main()