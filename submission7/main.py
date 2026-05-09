# Дані для завдання

# Словник для перевірки (варіант 6)
data = {"name": "Олена", "age": 20, "faculty": "КН"}

# Файл для запису помилок (варіант 8)
error_file = "error.log"

# Файл для зчитування (варіанти 5, 9)
input_file = "input.txt"

# Формат даних у файлі (варіант 9): "ім'я:вік" у кожному рядку

# Реалізуйте завдання тут

def is_leap_year(year):
    """Check if a year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def validate_date(date_str):
    """Validate date in dd-mm-yyyy format."""
    try:
        parts = date_str.strip().split('-')
        if len(parts) != 3:
            return False

        day = int(parts[0])
        month = int(parts[1])
        year = int(parts[2])

        # Validate month
        if month < 1 or month > 12:
            return False

        # Days in each month
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # Adjust February for leap year
        if is_leap_year(year):
            days_in_month[1] = 29

        # Validate day
        if day < 1 or day > days_in_month[month - 1]:
            return False

        # Validate year (reasonable range)
        if year < 1900 or year > 2100:
            return False

        return True
    except (ValueError, IndexError):
        return False

# Read date from stdin
date_input = input().strip()

if validate_date(date_input):
    print("Коректна дата")
else:
    print("Некоректна дата")
