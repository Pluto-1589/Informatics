def padded_zip(lists: list, padding=None):

    # if list of lists is empty return empty tuple
    if not lists:
        return ()
    # create an empty list for results
    res = []
    # iterate over the range of the longest list in the lits of lists
    for i in range(max(len(l) for l in lists)):
        # append to the empty results list a tuple with list at index i if i is smaller than length of list, else add padding
        res.append(tuple(l[i] if i < len(l) else padding for l in lists))
    return tuple(res)


l1 = [1, 2, 3, 4, 5]
l2 = [1.5, 2.5, 3.5, 4.5]
l3 = ["please", "send", "help"]
print(padded_zip([l1, l2, l3]))
print(padded_zip([l1, l2, l3, l1], "!"))
