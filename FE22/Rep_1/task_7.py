# Implement a class Market that keeps track of how much vendors are paying for having a stall at a market during a day.
class Market:

    def __init__(self) -> None:
        self._hour = 0
        self._vendors = 0
        self.profit = 0

    def progress_hour(self):

        self._hour += 1

    def stats(self):

        return {'number of vendors': self._vendors, 'hour': self._hour,
                'hourly profit': self.profit, 'total profit': self._vendors * self.profit}

    def add_vendor(self, fee):
        self.profit += fee
        self._vendors += 1

    def remove_vendor(self, fee):
        if fee not in self.d:
            raise Warning
        self.profit -= fee
        self._vendors -= 1


m = Market()
print(m.stats())
m.add_vendor(30)
m.add_vendor(5)
m.add_vendor(5)
print(m.stats())
m.progress_hour()
m.progress_hour()
m.progress_hour()
print(m.stats())
try:
    m.remove_vendor(11)
except:
    print("No vendor with that fee exists")
m.remove_vendor(5)
print(m.stats())
m.progress_hour()
print(m.stats())
