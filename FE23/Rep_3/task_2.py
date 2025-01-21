class Data:

    def __init__(self, data) -> None:
        self.data = data

    def compute(self, func_1, func_2):
        return (func_1(self.data), func_2(self.data))


objects = [1.7, 2.3, 3, 4]

d = Data(objects)
print(d.data is objects)
print(d.compute(sum, min))
print(d.compute(min, max))
