def sum_divisibles(limit: int, divisor: int,):

    a = 0

    # for i in the range of numbers 0 to tje limit number
    for i in range(0, limit + 1):
        # if i
        if i % divisor == 0:
            a += i
    return a


print(sum_divisibles(5, 2))
print(sum_divisibles(11, 5))
