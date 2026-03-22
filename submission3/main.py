num = [4, 2, 7, 2, 9, 4, 1, 7, 3]

a = int(input("Enter a number: "))

while a in num:
    num.remove(a)

print(num)