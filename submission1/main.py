# Implement task here
num1 = float(input())
num2 = float(input())

sum = num1 + num2
diff = num1 - num2
multiply = num1 * num2
if num2 == 0:
    print("False")
else:
    divide = num1 / num2

print(sum)
print(diff)
print(multiply)
print(divide)


if num1 > num2:
    answer = num1
if num1 < num2:
    answer = num2
else:
    answer = 'однакові'
print(answer)

