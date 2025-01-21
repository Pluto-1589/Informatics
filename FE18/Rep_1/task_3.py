def prod(x, y):

    if x == 0 or y == 0:
        return 0
    else:

        return x + prod(x, y - 1)


# print(prod(2, 0) == 0)
print(prod(5, 2) == 10)
