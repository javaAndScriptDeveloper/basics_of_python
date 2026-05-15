# Вводимо початок і кінець інтервалу
a = int(input("Введіть початок інтервалу: "))
b = int(input("Введіть кінець інтервалу: "))

primes = []

for num in range(a, b + 1):
    # Числа менші за 2 не є простими
    if num < 2:
        continue

    # Перевіряємо чи ділиться num на будь-яке число від 2 до sqrt(num)
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(num)

# Виводимо результат
print("Прості числа в інтервалі:", *primes)
