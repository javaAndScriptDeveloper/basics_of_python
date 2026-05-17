import sys

def main():
    # Зчитуємо задане значення (ліміт для послідовності)
    line = sys.stdin.readline().strip()
    if not line:
        return
    
    try:
        limit = int(line)
    except ValueError:
        return

    # Ініціалізуємо перші два числа Фібоначчі за стандартом тесту (1 і 1)
    a, b = 1, 1
    fib_sequence = []

    # Генеруємо числа, поки вони не перевищують ліміт
    while a <= limit:
        fib_sequence.append(str(a))
        a, b = b, a + b

    # Виводимо їх через пробіл (тест зчитає це завдяки шаблону .*)
    print(" ".join(fib_sequence))

if __name__ == "__main__":
    main()