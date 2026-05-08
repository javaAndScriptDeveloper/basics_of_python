import sys

def main():
    # Read all stdin, take the first token if present
    data = sys.stdin.read().strip().split()
    if not data:
        return  # no input, nothing to do

    try:
        celsius = float(data[0])
    except ValueError:
        return  # invalid input, exit silently

    fahrenheit = celsius * 9.0 / 5.0 + 32.0
    # Print integer if whole, otherwise print as float
    if fahrenheit.is_integer():
        print(int(fahrenheit))
    else:
        print(fahrenheit)

if __name__ == "__main__":
    main()
#234