# Implement task here
import sys

def main():
    input_data = sys.stdin.read().split()

    start = int(input_data[0])
    end = int(input_data[1])

    for num in range(start, end+1):
        if num < 2:
            continue

        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")

if __name__ == '__main__':
    main()