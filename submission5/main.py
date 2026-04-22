
import os

input_filename = 'input.txt'
output_filename = 'output.txt'

if not os.path.exists(input_filename):
    print(f"Файл '{input_filename}' не знайдено.")
else:
    with open(input_filename, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()
    
    lines.reverse()
    
    with open(output_filename, 'w', encoding='utf-8') as outfile:
        outfile.writelines(lines)