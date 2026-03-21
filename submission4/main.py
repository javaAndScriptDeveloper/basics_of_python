# Тестові значення:
# 3) Цельсій → Фаренгейт: 0, 100, 37

def celsius_to_fahrenheit(celsius_temp):
    '''
    Конвертує градуси Цельсія у Фаренгейти

    Аргументи: градуси Цельсія (float)

    Повертає: градуси Фаренгейта (float)
    '''

    return celsius_temp * 9 / 5 + 32

# Виклик функції для тестових значень і вивід результату
def main():
    print(celsius_to_fahrenheit(0))
    print(celsius_to_fahrenheit(100))
    print(celsius_to_fahrenheit(37))

if __name__ == '__main__':
    main()