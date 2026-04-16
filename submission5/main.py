# Дані для завдання

# Шлях до вхідного файлу
input_file = "input.txt"

# Шлях до вихідного файлу
output_file = "output.txt"

# Реалізуйте завдання тут
import os
def create_sample_file(filename: str) -> None:
    content = ["Line 1\n\nLine 2\n\n\nLine 3\n"]
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(content)

def process_text_File(input_file: str, output_file: str) -> None:
    with open(input_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    if not lines:
        print("Input file is empty")
        return None

    processed_lines = []
    for line in lines:
        empty_line = line.strip()
        if empty_line:
            processed_lines.append(empty_line + "\n")

    with open(output_file,"w", encoding="utf-8") as file:
        file.writelines(processed_lines)
        
def main():
    create_sample_file(input_file)
    process_text_File(input_file, output_file)

    if os.path.exists(output_file):
        print("Data inside:")
    with open(output_file, "r",encoding="utf-8") as file:
        print(file.read(),end="")
        
if __name__ == "__main__":
    main()