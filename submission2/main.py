x = int(input())
y = int(input())

for i in range(x, y+1):
    if not i % 2 == 0 and not i % 3 == 0 and not i == 1 or i == 2 or i == 3:
        print(i)

