# Дані для завдання
# Файл для зчитування (варіанти 5, 9)
input_file = "input.txt"

# Реалізуйте завдання тут
import os

log_file = "error.log"

def log_message(level, message):
    formatted_msg = f"{level}: [{message}]"
    print(formatted_msg)
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(formatted_msg + "\n")

def process_data(file_path):
    if not os.path.exists(file_path):
        return

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line_num, line in enumerate(file, 1):
                line = line.strip()
                if not line: continue
                
                try:
                    if ":" not in line:
                        raise ValueError("missing colon")
                    
                    name, age_str = line.split(":", 1)
                    age = int(age_str)
                    log_message("INFO", f"Data: {name}, Age: {age}")
                    
                except ValueError:
                    log_message("ERROR", f"ValueError at line {line_num}: incorrect data")

    except Exception as e:
        log_message("ERROR", f"Critical error: {e}")

def main():
    if os.path.exists(log_file):
        os.remove(log_file)
    process_data(input_file)

if __name__ == "__main__":
    main()