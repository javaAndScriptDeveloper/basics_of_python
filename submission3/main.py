def print_list(li):
    print(', '.join(str(item) for item in li))

# Список цілих чисел
numbers = [12, 7, 45, 3, 28, 15, 9, 33, 21]

# Значення для видалення зі списку
value_to_remove = 45

# Реалізуйте завдання тут
print_list(numbers)

numbers.remove(value_to_remove)

print_list(numbers)