# Дані для завдання

# Список цілих чисел
numbers = [12, 7, 45, 3, 28, 15, 9, 33, 21]

# Другий список цілих чисел
numbers2 = [50, 60, 70]

# Список з повторюваними елементами
numbers_with_duplicates = [4, 2, 7, 2, 9, 4, 1, 7, 3]

# Словник з іменами та віком
people = {"Олена": 25, "Іван": 30, "Марія": 22, "Петро": 35, "Анна": 28, "Сергій": 40}

# Значення для видалення зі списку
value_to_remove = 45

# Значення для пошуку в словнику
value_to_find = 30

# Реалізуйте завдання тут

# --- ЗАГАЛЬНЕ ЗАВДАННЯ ---
# 1. Об'єднання numbers та numbers2
# sum_numbers = numbers + numbers2
# print(sum_numbers)

# # 2. Видалення value_to_remove зі списку numbers
# if value_to_remove in numbers:
#     numbers.remove(value_to_remove)
#     print(numbers)

# # 3. Знайти вік для value_to_find у словнику people
# for name, age in people.items():
#     if age == value_to_find:
#         print(f"{name}, {age}")


# # ІНДИВІДУАЛЬНЕ ЗАВДАННЯ (Варіант 4)
# # Вивести елементи списку у зворотному порядку
print(list(reversed(numbers)))
print(list(reversed(numbers2)))
print(list(reversed(numbers_with_duplicates)))
