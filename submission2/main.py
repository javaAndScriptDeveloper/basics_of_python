# Implement task here
# Лабораторна робота №2 з теми Використання операторів умовного виконання та циклів у мові
# програмування Python.
# Варіант 1:
# Введення початкових даних
first_element = float(input())
diff = float(input())
element_count = int(input())

# За допомогою циклу for обчислюємо кожен елемент прогресії
for i in range(0, element_count):
    print(first_element)
    first_element = first_element + diff

