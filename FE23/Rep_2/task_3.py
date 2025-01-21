def merge_dicts(dicts: list, reverse_priority=False):
    """
    The function should return a dictionary resulting from merging all the dictionaries in dicts. In other words, the resulting dictionary should contain all items of all dictionaries in dicts. If multiple dictionaries in dicts contain the same key, then the value contained in the last dictionary containing that key (in terms of order within dicts) should take precedence, unless reverse_priority is True, in which case, the first dictionary containing that key should be used.
    """
    res = {}

    if reverse_priority:

        for d in reversed(dicts):
            for k, v in d.items():
                if k not in res:
                    res[k] = v
    else:

        for d in dicts:
            for k, v in d.items():
                if k not in res:
                    res[k] = v

    return res


d1 = {1: "a", 2: "b", 3: "c"}
d2 = {1: 1, 20: 2, 300: 3}
d3 = {1: "please", 2: "send", 300: "help"}
# {1: 'please', 2: 'send', 3: 'c', 20: 2, 300: 'help'}
print(merge_dicts([d1, d2, d3]))
# {1: 'a', 2: 'b', 300: 3, 20: 2, 3: 'c'}
print(merge_dicts([d1, d2, d3], True))
