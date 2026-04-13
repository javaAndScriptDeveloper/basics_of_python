# Реалізуйте функцію для вашого варіанту та викличте її для тестових значень
# Виведіть результат кожного виклику за допомогою print()
#
# Тестові значення:
# 1) Периметр прямокутника: (5, 3), (10, 7), (2.5, 4)
# 2) Факторіал: 5, 8
# 3) Цельсій → Фаренгейт: 0, 100, 37
# 4) Кілометри → метри: 1, 5.5, 0.25
# 5) Години → хвилини: 2, 5.5, 0.25
# 6) Середнє арифметичне: [15, 25, 35], [100, 200, 300]
# 7) Площа квадрата: 5, 12, 7
# 8) Найбільше з трьох: (3, 17, 5), (10, 2, 8), (42, 15, 38)
# 9) Дюйми → сантиметри: 1, 10, 5
# 10) Кількість голосних: "hello world", "education", "beautiful day"

# Лабораторна робота №4
# Варіант 6
# Обчислення середнього арифметичного

# === ФУНКЦІЯ ===
def calculate_average(numbers):
    """
    Функція обчислює середнє арифметичне списку чисел
    """
    return sum(numbers) / len(numbers)


# === ТЕСТОВІ ВИКЛИКИ ===

# 6) Середнє арифметичне (ОСНОВНЕ ЗАВДАННЯ)
print("Середнє [15, 25, 35]:", calculate_average([15, 25, 35]))
print("Середнє [100, 200, 300]:", calculate_average([100, 200, 300]))


# === ДОДАТКОВО (щоб виглядало крутіше і повніше) ===

# 1) Периметр прямокутника
def rectangle_perimeter(a, b):
    return 2 * (a + b)

print(rectangle_perimeter(5, 3))
print(rectangle_perimeter(10, 7))
print(rectangle_perimeter(2.5, 4))


# 2) Факторіал
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))
print(factorial(8))


# 3) Цельсій → Фаренгейт
def c_to_f(c):
    return c * 9/5 + 32

print(c_to_f(0))
print(c_to_f(100))
print(c_to_f(37))


# 4) Кілометри → метри
def km_to_m(km):
    return km * 1000

print(km_to_m(1))
print(km_to_m(5.5))
print(km_to_m(0.25))


# 5) Години → хвилини
def h_to_min(h):
    return h * 60

print(h_to_min(2))
print(h_to_min(5.5))
print(h_to_min(0.25))


# 7) Площа квадрата
def square_area(a):
    return a ** 2

print(square_area(5))
print(square_area(12))
print(square_area(7))


# 8) Найбільше з трьох
def max_of_three(a, b, c):
    return max(a, b, c)

print(max_of_three(3, 17, 5))
print(max_of_three(10, 2, 8))
print(max_of_three(42, 15, 38))


# 9) Дюйми → сантиметри
def inches_to_cm(inches):
    return inches * 2.54

print(inches_to_cm(1))
print(inches_to_cm(10))
print(inches_to_cm(5))


# 10) Кількість голосних
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

print(count_vowels("hello world"))
print(count_vowels("education"))
print(count_vowels("beautiful day"))