from math import pi


class Shape():

    def __init__(self) -> None:
        pass

    def area(self):
        return 0

    def description(self):
        return f"{type(self).__name__} with area {self.area()}"

# Now, implement Rectangle and Circle classes that extend Shape. Make sure that your implementations reuse description that is defined in the base class. Note: The area of a circle with radius r can be calculated with a = πr2, approximate π with 3


class Rectangle(Shape):

    def __init__(self, height, length) -> None:
        super().__init__()
        self.height = height
        self.length = length

    def area(self):
        return self.height * self.length

    def description(self):
        return super().description()


class Circle(Shape):

    def __init__(self, radius) -> None:
        super().__init__()
        self.radius = radius

    def area(self):
        return pi * self.radius * 2

    def description(self):
        return super().description()


class Square(Rectangle):

    def __init__(self, height, length, side) -> None:
        super().__init__(height, length)
        self. side = side

    def area(self):
        return self.side ** 2

    def description(self):
        return super().description()


# print(Rectangle(2, 5).description() == "Rectangle with area 10")
# print(Rectangle(2, 5).area() == 10)
# print(Circle(5).description() == "Circle with area 75")
# print(Circle(5).area() == 75)
