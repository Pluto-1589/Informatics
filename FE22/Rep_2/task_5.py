class Currency:

    def __init__(self, name: str, amount: float, rate: float):
        self.name = name
        self.amount = amount
        self.rate = rate

    def __eq__(self, other):

        if not isinstance(other, Currency):
            return NotImplemented
        else:
            conversion_self = self.amount * self.rate
            conversion_other = other.amount * other.rate

            return conversion_self == conversion_other


print(Currency("EUR", 15, 0.5) == Currency("GBP", 10, 0.75))  # True
print(Currency("EUR", 15, 0.5) != Currency("GBP", 15, 0.75))  # True
print(Currency("GBP", 1, 0.75) == Currency("GBP", 10, 0.75))  # False
print(Currency("CHF", 1.50, 0.78) == "Enough to buy a coffee")  # False
