# Реалізуйте функцію для вашого варіанту та викличте її для тестових значень
# Виведіть результат кожного виклику за допомогою print()
#
# Тестові значення:

# 3) Цельсій → Фаренгейт: 0, 100, 37

def celsius_to_fahrenheit(celsius):#виклик функції
    fahrenheit = (celsius * 9/5) + 32#формула для перетворення градусів Цельсія в Фаренгейти
    return fahrenheit#повертає результат


#a = int(input("your celsius: "))#питаємо що за градуси Цельсія хоче користувач ввести
#print("fahrenheit: ", round(celsius_to_fahrenheit(a)))#виводимо результат виклику функції для
                                               # введеного користувачем значення градусів Цельсія

#тестові значення

print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(100))
print(celsius_to_fahrenheit(37))