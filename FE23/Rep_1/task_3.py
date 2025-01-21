def merge_dicts(dicts: list, reverse_priority=False):

    dic = dict()

    if reverse_priority is False:

        for d in dicts:
            dic.update(d)

    else:
        dicts.reverse()

        for d in dicts:
            dic.update(d)

    return dic


d1 = {1: "a", 2: "b", 3: "c"}
d2 = {1: 1, 20: 2, 300: 3}
d3 = {1: "please", 2: "send", 300: "help"}
print(merge_dicts([d1, d2, d3]))
print(merge_dicts([d1, d2, d3], True))
