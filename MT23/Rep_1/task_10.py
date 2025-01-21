class Product:
    def __init__(self, name: str, cost: float, profit: float) -> None:
        self.name = name
        self.cost = cost
        self.profit = profit

    def sales_price(self):
        return self.cost + (self.profit * self.cost)

    def __str__(self) -> str:
        return f"{self.name} sells for {self.sales_price()}"

    def __repr__(self) -> str:
        return f"Product({self.name}, {self.cost}, {self.profit})"


p = Product("Smartphone", 1000, 0.1)
print(p.sales_price())
print(p)
print([p, Product("Dumbphone", 100, 0.2)])
