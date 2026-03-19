
# 8) Найбільше з трьох: (3, 17, 5), (10, 2, 8), (42, 15, 38)

def max_numbers():
    numbers = [(3, 17, 5), (10, 2, 8), (42, 15, 38)]
    max_num = max(numbers[0]), max(numbers[1]), max(numbers[2])
    return max_num
print(max_numbers())

