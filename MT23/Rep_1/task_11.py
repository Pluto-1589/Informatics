class Product():
    def __init__(self, name: str, price: float, discount: float) -> None:
        self.name = name
        self.price = price
        self.discount = discount

    def sales_price(self):
        return self.price - (self.price * self.discount)

    def __str__(self) -> str:
        return f"{self.name} sells for {self.sales_price():.2f}"

    def __repr__(self) -> str:
        return f"Product({self.name},{self.price:.2f},{self.discount})"


p = Product("Smartphone", 1000, 0.1)
print(p.sales_price())
print(p)
print([p, Product("Dumbphone", 100, 0.2)])
