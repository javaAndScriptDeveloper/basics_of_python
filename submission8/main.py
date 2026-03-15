# Лабораторна робота 8: Основи ООП

# Реалізуйте завдання тут
# ==========================================
# Індивідуальне завдання (Варіант 6)
# Клас для моделювання покупки в магазині з обчисленням загальної вартості
# ==========================================

class StorePurchase:
    def __init__(self):
        # Список для зберігання цін доданих товарів
        self.items_prices = []

    def add_item(self, name, price):
        # Додаємо ціну товару до списку
        self.items_prices.append(price)

    def calculate_total(self):
        # Обчислюємо загальну суму
        return sum(self.items_prices)

    def show_receipt(self):
        total = self.calculate_total()
        # Виводимо результат у форматі, який очікує bash-скрипт
        print(f"Загальна вартість: {int(total)}")

def main():
    purchase = StorePurchase()
    
    try:
        # 1. Читаємо кількість товарів
        num_items = int(input().strip())
        
        # 2. У циклі читаємо назву та ціну кожного товару
        for _ in range(num_items):
            item_name = input().strip()
            item_price = float(input().strip())
            
            # Додаємо товар до покупки
            purchase.add_item(item_name, item_price)
            
        # 3. Виводимо чек (суму)
        purchase.show_receipt()
        
    except EOFError:
        pass

if __name__ == "__main__":
    main()