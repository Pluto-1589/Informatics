def print_range(start, stop, step):

    # as long as start is greater than stop
    while start < stop:
        print(start)
        start = start + step


print(print_range(0, 5, 1))
print(print_range(5, 20, 3))
