import sys


def main():
    input_filename = 'input.txt'
    output_filename = 'output.txt'

    try:
        with open(input_filename, 'r') as f:
            data = f.read().split()

        numbers = [int(x) for x in data]

        numbers.sort()

        with open(output_filename, 'w') as f:
            f.write(" ".join(map(str, numbers)))

        print(" ".join(map(str, numbers)))

    except FileNotFoundError:
        input_data = sys.stdin.read().split()
        if input_data:
            numbers = sorted([int(x) for x in input_data])
            print(" ".join(map(str, numbers)))
    except Exception as e:
        pass


if __name__ == "__main__":
    main()