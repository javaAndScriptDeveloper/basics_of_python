# Реалізуйте функцію для вашого варіанту та викличте її для тестових значень
# Виведіть результат кожного виклику за допомогою print()
#
# Тестові значення:
# 9) Дюйми → сантиметри: 1, 10, 5

def inch_to_cm(inches: float) -> float:
    if inches < 0:
        return 0.0
    return round(inches*2.54,2)
test_values = [1,10,5]
for val in test_values:
    print(inch_to_cm(val))