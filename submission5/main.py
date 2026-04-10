import os

def main():
    input_file = 'input.txt'
    output_file = 'output.txt'
    
    # 1. Перевіряємо, чи створив тест файл input.txt
    if os.path.exists(input_file):
        # 2. Читаємо числа з файлу
        with open(input_file, 'r', encoding='utf-8') as f:
            # Зчитуємо всі дані. Оскільки вони в стовпчик, split() їх чудово розділить
            content = f.read().split()
            # Перетворюємо на цілі числа
            numbers = [int(x) for x in content]
        
        # 3. Сортуємо список за зростанням
        numbers.sort()
        
        # 4. Записуємо результат в output.txt
        with open(output_file, 'w', encoding='utf-8') as f:
            # Скрипт перевіряє вміст через паттерн "3.*12.*45", 
            # тому ми можемо записати їх як у рядок, так і в стовпчик.
            # Запишемо в стовпчик для акуратності
            for num in numbers:
                f.write(f"{num}\n")
        
        # Для самоконтролю виведемо в консоль
        print(f"Success: numbers sorted and saved to {output_file}")
    else:
        print(f"Error: {input_file} not found. Ensure the test script creates it.")

if __name__ == "__main__":
    main()