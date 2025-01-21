def count(l):

    total_count = 0

    for e in l:
        if isinstance(e, list):
            total_count += count(e)
        else:
            total_count += 1
    return total_count


# DO NOT SUBMIT THE LINES BELOW!
print(count([]) == 0)
print(count([[], []]) == 0)
print(count([1, "", [{}], [[True], 4]]) == 5)


print(count([]))
print(count([[], []]))
print(count([1, "", [{}], [[True], 4]]))
