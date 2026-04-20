import sys

def main():
    try:
        input_data = sys.stdin.read().split()
        
        if not input_data:
            return

        num1 = float(input_data[0])
        num2 = float(input_data[1])
        
        result = num1 / num2
        
        if result == int(result):
            print(int(result))
        else:
            print(result)
        
    except ZeroDivisionError:
        print("Помилка: ділення на нуль")
        
        with open("error.log", "w", encoding="utf-8") as f:
            f.write("ZeroDivisionError: division by zero")
            
    except (ValueError, IndexError):
        print("Помилка: некоректні дані")
        
    finally:
        pass

if __name__ == "__main__":
    main()