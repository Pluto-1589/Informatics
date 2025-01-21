class Currency:

    def __init__(self, name: str, amount: float, rate: float) -> None:
        self.name = name
        self.amount = amount
        self.rate = rate

    def __eq__(self, other: object) -> bool:
        # Two instances of Currency are equal if multiplying the amount with the rate results in the same value for both instances
        if not isinstance(other, Currency):
            return NotImplemented

        return self.amount * self.rate == other.amount * other.rate


print(Currency("EUR", 15, 0.5) == Currency("GBP", 10, 0.75))
print(Currency("EUR", 15, 0.5) != Currency("GBP", 15, 0.75))
print(Currency("GBP", 1, 0.75) == Currency("GBP", 10, 0.75))
print(Currency("CHF", 1.50, 0.78) == "Enough to buy a coffee")
