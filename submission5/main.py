import os

def main():
    input_filename = "input.txt"
    output_filename = "output.txt"

    if not os.path.exists(input_filename):
        with open(input_filename, "w", encoding="utf-8") as f:
            f.write("Перший рядок\n\nДругий рядок\n\n\nТретій рядок\n")
            
    try:
        with open(input_filename, "r", encoding="utf-8") as infile:
            lines = infile.readlines()

        non_empty_lines = [line for line in lines if line.strip() != ""]
        with open(output_filename, "w", encoding="utf-8") as outfile:
            outfile.writelines(non_empty_lines)
            
        print("Успіх: Порожні рядки видалено!")
        
    except Exception as e:
        print(f"Сталася помилка при роботі з файлами: {e}")

if __name__ == "__main__":
    main()