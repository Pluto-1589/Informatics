def length(iterable):
    #  compute the length of iterable recursively. iterable, which can be a list, tuple or string

    if iterable in [[], "", ()]:
        return 0
    return 1 + length(iterable[1:])


print(length([1, 2, [3, 4]]))
print(length(("a", 1, 2, None)))
print(length("oh dear"))
