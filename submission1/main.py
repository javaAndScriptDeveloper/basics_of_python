a = float(input("Enter the first number: "))
b = float(input("Enter another number: "))

sum = a + b
diff = a - b
divide = a / b
multiply = a * b

print("Sum:", sum)
print("Difference:", diff)
print("Division:", divide)
print("Multiplication:", multiply)

if sum % 2 == 0:
    print("Парне")
else:
    print("Непарне")

if diff % 2 == 0:
    print("Парне")
else:
    print("Непарне")

if divide % 2 == 0:
    print("Парне")
else:
    print("Непарне")

if multiply % 2 == 0:
    print("Парне")
else:
    print("Непарне")
