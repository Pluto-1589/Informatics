def padded_zip(lists: list, padding=None):
    # return a tuple of tuples where the i-th tuple contains the i-th element from each of the lists contained in lists

    if not lists:
        return ()
    else:
        res = []
        for i in range(max(len(l) for l in lists)):
            res.append(tuple(l[i] if i < len(l) else padding for l in lists))

        return tuple(res)


l1 = [1, 2, 3, 4, 5]
l2 = [1.5, 2.5, 3.5, 4.5]
l3 = ["please", "send", "help"]
print(padded_zip([l1, l2, l3]))
print(padded_zip([l1, l2, l3, l1], "!"))

# ((1, 1.5, 'please'), (2, 2.5, 'send'), (3, 3.5, 'help'), (4, 4.5, None), (5, None, None))
# ((1, 1.5, 'please', 1), (2, 2.5, 'send', 2), (3, 3.5, 'help', 3), (4, 4.5, '!', 4), (5, '!', '!', 5))
