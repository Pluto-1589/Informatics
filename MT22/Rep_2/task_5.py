def duplicate_every(l, n):

    for i in len(l):
        if i == n:
            (l.insert(i, l[i],))

    return l


print(duplicate_every([1, 3, 4, 5], 2))
print(duplicate_every([1, 4, 5, 4, 3, 2, 1], 3))
