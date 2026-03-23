# Загальне завдання 
print("--- Загальне завдання ---")

# Допоміжна функція, щоб цілі числа (наприклад 10.0) ставали int (10)
def parse_input(prompt):
    val = float(input(prompt))
    return int(val) if val.is_integer() else val

num1 = parse_input("Введіть перше число: ")
num2 = parse_input("Введіть друге число: ")

print(f"Сума: {num1 + num2}")
print(f"Різниця: {num1 - num2}")
print(f"Добуток: {num1 * num2}")

# Індивідуальне завдання 
print("\n--- Індивідуальне завдання (Варіант 4) ---")

# Перевірка на нуль для уникнення ZeroDivisionError
if num2 != 0:
    division_result = num1 / num2
    
    # Якщо результат ділення є цілим числом (напр. 5.0), конвертуємо в int (5)
    if isinstance(division_result, float) and division_result.is_integer():
         division_result = int(division_result)
         
    print(f"Результат ділення {num1} на {num2} дорівнює: {division_result}")
else:
    # Текст помилки ідеально збігається з патерном "[Дд]ілення на нуль неможливе"
    print("Помилка: ділення на нуль неможливе!")