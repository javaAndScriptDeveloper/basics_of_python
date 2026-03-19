# Implement task here
# Просимо користувача ввести перший член прогресії, різницю та кількість членів для обчислення
first_term = float(input("Enter first term of the progression: "))
difference = float(input("Enter the common difference: "))
num_terms = int(input("Enter the number of terms to calculate: "))

# Обчислюємо та виводимо кожен член прогресії
for n in range(num_terms):
    term = first_term + n * difference
    print(f"Term {n + 1}: {term}")

