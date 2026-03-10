# Дані для завдання

# Шлях до вхідного файлу
input_file = "input.txt"

# Шлях до вихідного файлу
output_file = "output.txt"

# Слово для пошуку (варіант 5)
word_to_find = "Python"

# Слово для заміни та нове слово (варіант 6)
word_to_replace = "World"
replacement_word = "Ukraine"

# Новий рядок для додавання (варіант 7)
new_line = "Новий рядок додано"

# Новий вміст для перезапису (варіант 10)
new_content = "Файл перезаписано"

# Реалізуйте завдання тут
with open('input.txt', 'r', encoding='utf-8') as file:
    numbers = [float(x) for x in file.read().split()]
if len(numbers) > 0:
    # Рахуємо середнє арифметичне
    average = sum(numbers) / len(numbers)
    result = f"Середнє значення: {average:.2f}"
    
    print(result) 
    
    with open('output.txt', 'w', encoding='utf-8') as file:
        file.write(result)
else:
    print("Файл порожній.")