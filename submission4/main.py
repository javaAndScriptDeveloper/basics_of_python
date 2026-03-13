def factorial(n):
    if n == 0:
        return 1 
    
    result = 1
    for i in range(1, n + 1):
        result = result * i 
    return result 

print("Обчислення факторіала числа")
print("Вводьте числа. Щоб завершити програму, напишіть 'stop'")
try: 

    while True: 
        value = input("Введіть число: ")  

        if value.lower() == "stop":  
            print("Програму завершено")
            break 

        num = int(value) 

        if num < 0: 
            print("Факторіал для від’ємних чисел не існує")
            continue

        print(num, "! =", factorial(num))
except: 
     print("помилка, введіть коректні числа")
