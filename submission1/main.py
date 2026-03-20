# Implement task here
def celsius_to_fahrenheit():
    try:
        celsius = float(input("Введіть температуру в градусах Цельсія: "))
    except ValueError:
        print("Будь ласка, введіть число.")
        return

    print(f"\nКонвертуємо {celsius}°C у Фаренгейти крок за кроком:")
    
    # 1. Множення
    step1 = celsius * 9
    print(f"1. Множення: {celsius} * 9 = {step1}")
    
    # 2. Ділення
    step2 = step1 / 5
    print(f"2. Ділення: {step1} / 5 = {step2}")
    
    # 3. Додавання
    fahrenheit = step2 + 32
    print(f"3. Додавання: {step2} + 32 = {fahrenheit}°F")
    
    # 4. Віднімання
    difference = fahrenheit - celsius
    print(f"4. Віднімання: Різниця між числовими значеннями ({fahrenheit} - {celsius}) = {difference}")
    
    print("-" * 40)
    print(f"Відповідь: {celsius}°C дорівнює {fahrenheit}°F")

# Запуск програми
if __name__ == "__main__":
    celsius_to_fahrenheit()