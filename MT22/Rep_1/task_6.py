def product(xs: list, ys: list):
    for x in xs:
        for y in ys:
            print(x * y)


print(product([5], [10, 11]))
print(product([2, 3, 4], [1, 10, 20]))
