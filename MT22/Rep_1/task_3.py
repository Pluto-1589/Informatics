def length(iterable):

    # if iterable is an an empty list, tuple or string
    if iterable in [[], (), ""]:
        # return 0
        return 0
    # if iterable is not empty
    else:
        # return 1 plus the recursive call starting at the second element
        return 1 + length(iterable[1:])


print(length([1, 2, [3, 4]]))
print(length(("a", 1, 2, None)))
print(length("oh dear"))
