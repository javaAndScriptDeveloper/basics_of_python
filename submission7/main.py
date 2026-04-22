import logging

logging.basicConfig(
    filename='error.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

class NegativeNumberError(Exception):
    """Користувацький виняток для від'ємних чисел."""
    pass

def check_number():
    try:
        user_input = input("Введіть число: ")
        number = float(user_input)

        if number < 0:
            raise NegativeNumberError(f"Помилка: число {number} є від'ємним.")
        
        print(f"Число {number} є додатним (або нулем).")

    except ValueError as e:
        error_msg = f"Помилка введення: '{user_input}' не є числом."
        print(error_msg)
        logging.error(error_msg)
        
    except NegativeNumberError as e:
        error_msg = str(e)
        print(error_msg)
        logging.error(error_msg)
        
    except Exception as e:
        error_msg = f"Виникла непередбачувана помилка: {e}"
        print(error_msg)
        logging.error(error_msg)
        
    finally:
        print("Програма завершила виконання.")

if __name__ == "__main__":
    check_number()