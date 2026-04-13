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
# Варіант 6
# Перевірка наявності значення у словнику + робота зі списками

numbers = [12, 7, 45, 3, 28, 15, 9, 33, 21]
numbers2 = [50, 60, 70]
numbers_with_duplicates = [4, 2, 7, 2, 9, 4, 1, 7, 3]

people = {
    "Олена": 25,
    "Іван": 30,
    "Марія": 22,
    "Петро": 35,
    "Анна": 28,
    "Сергій": 40
}

value_to_remove = 45
value_to_find = 30

# Видалення елемента зі списку
if value_to_remove in numbers:
    numbers.remove(value_to_remove)
    print(f"Елемент {value_to_remove} видалено зі списку.")
else:
    print(f"Елемент {value_to_remove} не знайдено.")

print("Оновлений список:", numbers)


combined_list = numbers + numbers2
print("Об'єднаний список:", combined_list)


unique_list = list(set(numbers_with_duplicates))
print("Список без повторів:", unique_list)


# Перевірка наявності значення у словнику
if value_to_find in people.values():
    print(f"Значення {value_to_find} знайдено у словнику.")
else:
    print(f"Значення {value_to_find} не знайдено у словнику.")