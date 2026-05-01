import os

input_filename = 'input.txt'
output_filename = 'output.txt'

if os.path.exists(input_filename):
    with open(input_filename, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    processed_lines = [line for line in lines if line.strip() != '']

    with open(output_filename, 'w', encoding='utf-8') as outfile:
        outfile.writelines(processed_lines)
else:
    pass