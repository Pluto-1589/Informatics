def padded_dict(keys, values: list, padding=None):

    # create new dictionary
    d = {}

    # iterate over the range of length of key list
    for i in range(len(keys)):
        # try assigning value at index of range of length keys in values list to val
        try:
            val = values[i]
        except IndexError:
            val = padding

        d[keys[i]] = val

    return d


print(padded_dict([1, "b", 3], [55, 66, 77]))
print(padded_dict([1, "b", 3], [55]))
print(padded_dict([1, "b"], [55, 66, 77]))
