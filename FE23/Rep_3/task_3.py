def merge_dicts(dicts: list, reverse_priority=False):
    # return a dictionary resulting from merging all the dictionaries in dicts

    # assign empty dict to res
    res = {}

    # if true
    if reverse_priority:
        # reverse the list of dicts
        dicts = reversed(dicts)
    # iterate over each dict in dicts
    for d in dicts:
        # for key and val in dict items
        for k, v in d.items():
            # key has value v
            res[k] = v

    return res


d1 = {1: "a", 2: "b", 3: "c"}
d2 = {1: 1, 20: 2, 300: 3}
d3 = {1: "please", 2: "send", 300: "help"}
# {1: 'please', 2: 'send', 3: 'c', 20: 2, 300: 'help'}
print(merge_dicts([d1, d2, d3]))
# {1: 'a', 2: 'b', 300: 3, 20: 2, 3: 'c'}
print(merge_dicts([d1, d2, d3], True))


# Solutions:

def merge_dicts(dicts, reverse_priority=False):
    res = {}
    if reverse_priority:
        dicts = reversed(dicts)
    for d in dicts:
        for k, v in d.items():
            res[k] = v
    return res

# or


def merge_dicts(dicts, reverse_priority=False):
    res = {}
    for d in dicts:
        if reverse_priority:
            res = d | res
        else:
            res = res | d
    return res
