def add(n):
    def addition(x):
        return n + x

    return addition


print(add(3)(10))
print(add(-5)(15))
