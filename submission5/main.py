# Дані для завдання

# Шлях до вхідного файлу
input_file = "input.txt"

# Шлях до вихідного файлу
output_file = "output.txt"


#варіант 3
'''Написати програму, яка зчитує дані з текстового файлу та записує їх у новий
файл, виконуючи певні перетворення (наприклад, переведення всіх літер у
нижній регістр).'''

# відкриваємо файл і зчитуємо числа
with open("input.txt", "r") as file:
    numbers = [float(line.strip()) for line in file if line.strip()]

# перевірка щоб не було ділення на 0
if numbers:
    average = sum(numbers) / len(numbers)

    with open("output.txt", "w", encoding="utf-8") as out_file:
        out_file.write(f"Середнє значення: {average}\n")

    print("Готово! Результат записано в output.txt")
else:
    print("Файл порожній або немає чисел")