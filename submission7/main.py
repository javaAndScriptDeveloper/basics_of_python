try:
    user_input = input() 
    if not user_input:
        raise ValueError("Помилка! Список порожній")
        
    print(user_input)
except ValueError as err: 
    print(err)