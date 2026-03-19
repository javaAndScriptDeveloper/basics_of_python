numbers = [223, 22, 45, 30, 28, 150, 90000, 33, 24]

min_value = numbers[0]

for n in numbers:
    if n < min_value:
        min_value = n

print(min_value)
