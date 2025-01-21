class BankAccount:

    def __init__(self, balance=0, limit=0) -> None:
        self.balance = balance
        # raise an AssertionError when a negative credit limit is provided in the constructor
        if limit < 0:
            raise AssertionError("Cannot provide a negative credit limit")
        self.limit = limit

    def available(self):
        # available will report the maximum amount that is available for a withdrawal.
        difference = self.balance + self.limit

        if difference > self.limit:
            return f"Available to withdraw: {difference}"
        else:
            return "Withdraw exceeds the allowed credit limit - Cannot withdraw money at the current moment."

    def deposit(self, amount):

        self.balance += amount

    def withdraw(self, amount):
        # AssertionError when a withdraw exceeds the allowed credit limit
        if amount > self.limit:
            raise AssertionError("Withdraw exceeds the allowed credit limit")
        else:
            self.balance -= amount


# example usage
acc = BankAccount(100)
print(acc.balance)  # prints ’0’
print(acc.available())  # prints ’100’
acc.deposit(30)  # balance: 30, available: 130 (illustration, no "print")
acc.withdraw(40)  # balance: -10, available: 90 (illustration, no "print")
acc.withdraw(91)  # AssertionError
