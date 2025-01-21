from abc import ABC, abstractmethod


class Restaurant:

    def __init__(self, name):
        self.name = name


class Staff(ABC):
    # regardless of type, any staff works for a specific restaurant and has a unique employee number (101 for the first employee, 102 for the second, and so on). Furthermore, each staff holds a record of all shifts worked in the past. When a shift is worked, the number of hours is added to the shift record. Each staff also provides a way to determine the total salary earned by the staff, which is calculated depending on the type of staff.

    staff_id = 100

    def __init__(self, name, staff_record, base_salary):
        self.name = name
        Staff.staff_id += 1
        self.number = Staff.staff_id
        self.staff_record = [staff_record]
        self.current_shift = []
        self.base_salary = base_salary

    def work(self, hours):
        self.current_shift.append(hours)

    def shifts(self):
        return self.current_shift

    @abstractmethod
    def salary(self):
        pass

    def __str__(self):
        return f"Staff working for {self.name} with salary {self.salary()}"


# When a shift is worked, the number of hours is added to the shift record. Each staff also provides a way to determine the total salary earned by the staff, which is calculated depending on the type of staff.

# A server receives a base salary plus an hourly salary for each hour worked.
class Server(Staff):

    def __init__(self, name, staff_record, base_salary):
        super().__init__(name, staff_record, base_salary)

    def salary(self):
        for i in self.staff_record:

            return sum(self.current_shift) + i * self.base_salary

# For dish washers, the salary is computed the same way as for servers, but with a 10% deduction.


class Dishwasher(Staff):

    def __init__(self, name, staff_record, base_salary):
        super().__init__(name, staff_record, base_salary)

    def salary(self):
        for i in self.staff_record:

            return (sum(self.current_shift) + i * self.base_salary) - ((sum(self.current_shift) + i * self.base_salary) * 0.1)

# A cook receives the same salary, no matter how many hours are worked.


class Cook(Staff):

    def __init__(self, name, staff_record, base_salary):
        super().__init__(name, staff_record, base_salary)

    def salary(self):
        return self.base_salary


restaurant = Restaurant("Mc Ronalds")

cook = Cook(restaurant, 3200)
cook.work(10)
cook.work(50)
print(cook.number)  # 101
print(cook.shifts)  # [10, 50]
print(type(cook.shifts))  # <class 'list'>
print(cook.salary())  # 3200
print(cook)  # Staff working for Mc Ronalds with salary 3200

server = Server(restaurant, 100, 9.50)
server.work(10)
server.work(50)
print(server.number)  # 102
print(server.shifts)  # [10, 50]
print(server.salary())  # (100 + 60*9.50) # 670.0

washer = Dishwasher(restaurant, 100, 9.50)
washer.work(10)
washer.work(50)
print(washer.number)  # 103
print(washer.shifts)  # [10, 50]
print(washer.salary())  # (100 + 60*9.50) * 0.9 # 603.0
