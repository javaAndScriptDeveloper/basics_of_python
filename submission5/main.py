# Шлях до вхідного файлу
input_file = "input.txt"

# Шлях до вихідного файлу
output_file = "output.txt"

# РЗчитування чисел з вхідного файлу 
# та запис їх середнього у вихідний файл
import os

if os.path.exists(input_file):
    mean_value = None

    with open(input_file, 'r', encoding='utf-8') as infile:
        numbers = infile.read()
        numbers = numbers.split()

        num_sum = 0
        for num in numbers:
            num = int(num)
            num_sum += num

            if numbers:
                mean_value = num_sum / len(numbers)
            else:
                print('Файл порожній')

    with open(output_file, 'w', encoding='utf-8') as outfile:
        if mean_value != None:
            outfile.write(str(mean_value))
        else:
            outfile.write()
else:
    print('Файлу з такою назвою не існує')