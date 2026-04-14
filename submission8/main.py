# Лабораторна робота 8: Основи ООП

# Реалізуйте завдання тут
# Лабораторна робота №8
# Варіант 6
# Моделювання покупки в магазині

class Purchase:
    # Конструктор класу
    def __init__(self, product_name, price, quantity):
        self.product_name = product_name  # назва товару
        self.price = price                # ціна за одиницю
        self.quantity = quantity          # кількість товару

    # Метод для обчислення загальної вартості
    def calculate_total(self):
        return self.price * self.quantity

    # Метод для виведення інформації про покупку
    def show_info(self):
        print("Товар:", self.product_name)
        print("Ціна за одиницю:", self.price)
        print("Кількість:", self.quantity)
        print("Загальна вартість:", self.calculate_total())


# Створення об'єкта класу
purchase1 = Purchase("Зошит", 25, 4)

# Виклик методу для виведення інформації
purchase1.show_info()