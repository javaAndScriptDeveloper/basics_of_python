try:
    user_str_list = input("Введіть список чисел через пробіл ").split()
    user_num_list = [int(i) for i in user_str_list]

    if not user_num_list:
        raise ValueError("Список порожній")

except ValueError as e:
    print(e)

else:
    print(user_num_list)