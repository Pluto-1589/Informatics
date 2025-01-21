# Solution

from abc import ABC, abstractmethod


class Driver:
    counter = 1001

    def __init__(self, name):
        self.name = name
        self.number = Driver.counter
        Driver.counter += 1


class Transport(ABC):
    def __init__(self, driver):
        self.driver = driver
        self.trips = []

    def trip(self, km):
        self.trips.append(km)

    @abstractmethod
    def total_cost(self):
        pass

    def __str__(self):
        return f"Transport revenue: {self.total_cost()} (driver: {self.driver.name})"


class Taxi(Transport):
    def __init__(self, driver, trip_fee, km_fee):
        super().__init__(driver)
        self.trip_fee = trip_fee
        self.km_fee = km_fee

    def total_cost(self):
        return sum(self.trips) * self.km_fee + len(self.trips) * self.trip_fee


class DiscountTaxi(Taxi):
    def total_cost(self):
        return super().total_cost() * 0.8


class Shuttle(Transport):
    def __init__(self, driver, day_fee):
        super().__init__(driver)
        self.day_fee = day_fee

    def total_cost(self):
        return self.day_fee


# examples
driver = Driver("Travis Bickle")
driver = Driver("Korben Dallas")
print(driver.number)
