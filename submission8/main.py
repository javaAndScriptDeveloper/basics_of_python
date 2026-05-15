# Лабораторна робота 8: Основи ООП

# Реалізуйте завдання тут
class Program:
    def main(self):
        products = ConsoleInterface.purchase_input()
        purchase = Purchase(products)
        total_price = purchase.get_total_price()
        print(f"Загальна вартість: {total_price}")


class ConsoleInterface:
    @staticmethod
    def purchase_input():
        products = []
        amount = int(input("Введіть кількість товарів: "))
        for i in range(amount):
            product = ConsoleInterface.product_input()
            products.append(product)
        return products

    @staticmethod
    def product_input():
        product_name = input("Введіть назву товару: ")
        product_price = float(input("Введіть ціну товару: "))
        return Product(product_name, product_price)


class Purchase:
    def __init__(self, products: list["Product"]):
        self.products = products

    def get_total_price(self):
        return sum(product.price for product in self.products)


class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price


if __name__ == "__main__":
    Program().main()
