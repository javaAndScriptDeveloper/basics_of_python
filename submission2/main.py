start = int(input("Введіть початкове число інтервалу: "))
end = int(input("Введіть кінцеве число інтервалу: "))

print(f"\nПрості числа в інтервалі від {start} до {end}:")

# Перебір чисел у заданому діапазоні
for num in range(start, end + 1):
    # Прості числа завжди більші за 1
    if num > 1:
        is_prime = True
        
        # Перевіряємо наявність дільників
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break  # Якщо знайдено дільник, перериваємо цикл
                
        # Якщо число залишилось простим, виводимо його
        if is_prime:
            print(num, end=" ")
            