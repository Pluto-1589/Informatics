import math


class Data:

    def __init__(self, data: list) -> None:
        self.data = data

    def compute(self, func):

        res = []

        for i in self.data:
            res.append(func(i))

        return res


objects = [1.7, 2.3, 3, 4]
d = Data(objects)
print(d.data is objects)
print(d.compute(str))
print(d.compute(math.floor))
