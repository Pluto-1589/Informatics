class Market:

    def __init__(self):
        self.num_vendors = 0
        self.hours = 0
        self.hourly_profit = 0
        self.total_profit = 0

        self.tracking_vendors = []

    def progress_hour(self):
        # runs the clock one hour forward (the clock starts at zero).
        self.hours += 1
        self.total_profit += self.hourly_profit

    def stats(self):

        return {'number of vendors': self.num_vendors, 'hour': self.hours, 'hourly profit': self.hourly_profit, 'total profit': self.total_profit}

    def add_vendor(self, hourly_rate):

        self.num_vendors += 1
        self.hourly_profit += hourly_rate

        self.tracking_vendors.append(hourly_rate)

    def remove_vendor(self, hourly_rate):
        if not hourly_rate in self.tracking_vendors:
            raise Warning("No vendor with that fee exists")
        else:
            self.tracking_vendors.remove(hourly_rate)
            self.num_vendors -= 1
            self.hourly_profit -= hourly_rate


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

# {'number of vendors': 0, 'hour': 0, 'hourly profit': 0, 'total profit': 0}
# {'number of vendors': 3, 'hour': 0, 'hourly profit': 40, 'total profit': 0}
# {'number of vendors': 3, 'hour': 3, 'hourly profit': 40, 'total profit': 120}
# No vendor with that fee exists
# {'number of vendors': 2, 'hour': 3, 'hourly profit': 35, 'total profit': 120}
# {'number of vendors': 2, 'hour': 4, 'hourly profit': 35, 'total profit': 155}
