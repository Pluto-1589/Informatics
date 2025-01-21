def duplicates_of(lst, xs):

    count = 0

    for l in lst:
        for x in xs:
            if l == x:
                count += 1

    return count


print(duplicates_of([], []))
print(duplicates_of([1], [1]))
print(duplicates_of([True, True], [True]))
print(duplicates_of([1, 1, 'hello', 3], [1, 'hello', 1]))
