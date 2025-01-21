def ints_divisible_by(ints, by):
    # The function should return a list of numbers from ints containing only those which are divisible by by (in the original order).

    return [n for n in ints if n % by == 0]


print(ints_divisible_by(range(10), 3))
print(ints_divisible_by(range(20), 5))
print(ints_divisible_by([21, 2, 3, 33, 123], 3))
