def is_leap_year(year: int) -> bool:
    """Перевіряє, чи є рік високосним."""
    # Рік високосний, якщо ділиться на 4 і не ділиться на 100,
    # АБО якщо ділиться на 400.
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def main():
    try:
        # Введення даних
        line = input("Введіть рік: ")
        if not line:
            return
            
        year = int(line)
        
        # Розрахунки та виведення результату
        if is_leap_year(year):
            print(f"Рік {year} — високосний")
        else:
            print(f"Рік {year} — не високосний")
            
    except ValueError:
        print("Помилка: введіть ціле число")

if __name__ == "__main__":
    main()