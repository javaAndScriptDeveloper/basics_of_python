import logging
import os


logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("error.log", encoding="utf-8"), 
        logging.StreamHandler()
    ]
)

def check_format(filename):
    if not os.path.exists(filename):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("Олександр, 20\nМарія, КН\nІван, 21\nПросто текст без коми\n")

    print(f"Починаємо перевірку файлу {filename}...\n")

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
            for line_num, line in enumerate(lines, 1):
                line = line.strip()
                if not line:
                    continue
                    
                try:
                    parts = line.split(',')
                    if len(parts) != 2:
                        raise ValueError("Неправильна кількість елементів. Очікується 2 (через кому).")
                        
                    name = parts[0].strip()
                    age_str = parts[1].strip()
                    age = int(age_str)
                    
                    if age <= 0 or age > 120:
                        raise ValueError(f"Неприпустимий вік: {age}")
                        
                    print(f"✅ Рядок {line_num} правильний: {name} ({age} років)")
                    
                except ValueError as ve:
                    logging.error(f"Помилка формату у рядку {line_num} ('{line}'): {ve}")

    except FileNotFoundError as fnfe:
        logging.error(f"Критична помилка: Файл не знайдено - {fnfe}")
    except PermissionError as pe:
        logging.error(f"Критична помилка: Немає прав доступу до файлу - {pe}")
    except Exception as e:
        logging.error(f"Неочікувана помилка при роботі з файлом: {e}")

if __name__ == "__main__":
    input_file = "input.txt"
    check_format(input_file)