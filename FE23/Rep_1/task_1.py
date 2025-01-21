import math


class Data():
    def __init__(self, data) -> None:
        self.data = data

    def compute(self, f):

        l = []

        for i in self.data:
            l.append(f(i))

        return l


objects = [1.7, 2.3, 3, 4]
d = Data(objects)
print(d.data is objects)
print(d.compute(str))
print(d.compute(math.floor))
