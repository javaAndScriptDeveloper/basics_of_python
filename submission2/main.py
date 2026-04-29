# Implement task here
n = int(input("Введіть максимальне значення: "))

a, b = 0, 1
print("Послідовність Фібоначчі:")
while a <= n:
    print(a)
    a, b = b, a+b