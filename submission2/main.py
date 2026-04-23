import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    try:
        n = int(input_data[0])
        if n < 0:
            return

        factorial = 1
        for i in range(1, n + 1):
            factorial *= i

        print(factorial)

    except (ValueError, IndexError):
        pass

if __name__ == "__main__":
    main()