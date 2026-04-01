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

# 1. Видалення всіх повторюваних елементів зі списку
unique_numbers = list(set(numbers_with_duplicates))

# 2. Видалення заданого значення зі списку numbers
if value_to_remove in numbers:
    numbers.remove(value_to_remove)

# 3. Використання другого списку (наприклад, об'єднання з першим)
combined_numbers = numbers + numbers2

# 4. Пошук у словнику імені людини за її віком
found_people = [name for name, age in people.items() if age == value_to_find]

print("--- Результати обчислень ---\n")

print("1. Видалення дублікатів:")
print(f"Оригінальний список: {numbers_with_duplicates}")
print(f"Очищений список:     {unique_numbers}\n")

print("2. Робота з основними списками:")
print(f"Список 'numbers' після видалення числа {value_to_remove}: {numbers}")
print(f"Об'єднаний список (numbers + numbers2):       {combined_numbers}\n")

print("3. Пошук у словнику:")
if found_people:
    print(f"Людина(и) з віком {value_to_find} років: {', '.join(found_people)}")
else:
    print(f"Людей з віком {value_to_find} років не знайдено.")
