# Implement task here
import sys

def main():
    try:
        # Reading two numbers from standard input
        line1 = sys.stdin.readline().strip()
        line2 = sys.stdin.readline().strip()
        
        if not line1 or not line2:
            return

        num1 = float(line1)
        
        num2 = float(line2)
        

        # Logical check for division by zero as per variant requirements
        if num2 == 0:
            print("Ділення на нуль неможливе")
        else:
            result = num1 / num2
            # Use :g to format the number cleanly (e.g., 5.0 becomes 5) !
            print(f"{result:g}")

    except ValueError:
        print("Помилка: введіть коректні числа!")

if __name__ == "__main__":
    main()
