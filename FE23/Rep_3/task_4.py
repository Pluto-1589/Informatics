def padded_zip(lists: list, padding=None):

    if not lists:
        return ()
    else:
        res = []

        # iterate over the range of the length of the longest list in lists
        for i in range(max(len(l) for l in lists)):
            # append to res a tuple containing the ith element of each list, or padding if i exceeds the list's length
            res.append(tuple(l[i] if i < len(l) else padding for l in lists))

        return res


l1 = [1, 2, 3, 4, 5]
l2 = [1.5, 2.5, 3.5, 4.5]
l3 = ["please", "send", "help"]
# ((1, 1.5, 'please'), (2, 2.5, 'send'), (3, 3.5, 'help'), (4, 4.5, None), (5, None, None))
print(padded_zip([l1, l2, l3]))
# ((1, 1.5, 'please', 1), (2, 2.5, 'send', 2), (3, 3.5, 'help', 3), (4, 4.5, '!', 4), (5, '!', '!', 5))
print(padded_zip([l1, l2, l3, l1], "!"))


# Solutions:

def padded_zip(lists, padding=None):
    if not lists:
        return ()

    res = []

    for i in range(max(len(l) for l in lists)):
        this = []
        for l in lists:
            try:                       # if i < len(l):
                this.append(l[i])
            except IndexError:         # else:
                this.append(padding)
        res.append(tuple(this))
    return tuple(res)

# or


def padded_zip(lists, padding=None):
    if not lists:
        return ()
    res = []
    for i in range(max(len(l) for l in lists)):
        res.append(tuple(l[i] if i < len(l) else padding for l in lists))
    return tuple(res)

# or simply


def padded_zip(lists, padding=None):
    from itertools import zip_longest
    return tuple(zip_longest(*lists, fillvalue=padding))
