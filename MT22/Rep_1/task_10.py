def duplicate_every(l: list, n: int):

    # Implement a function duplicate_every which takes two parameters: a list l and a positive integer n. The function should return a list containing the elements from l but with every n'th element occuring twice. For example, if n is 3, every third element should be repeated once.

    # initialize empty list
    res = []
    # loop over l while keeping track of its index
    for i, item in enumerate(l):
        # check if 1 plus i is a multiple of n
        if (i+1) % n == 0:
            # add to list
            res.append(item)
        # add to list regardless of condition
        res.append(item)

    return res


print(duplicate_every([1, 3, 4, 5], 2))
print(duplicate_every([1, 4, 5, 4, 3, 2, 1], 3))
