from collections import Counter


def rev_idx(words):

    words = [w.lower() for w in words]

    res_dict = {}

    for v, k in enumerate(words):
        if k not in res_dict:
            res_dict[k] = [v]
        else:
            res_dict[k].append(v)

    return res_dict


print(rev_idx([]) == {})
print(rev_idx(["a", "b"]) == {"a": [0], "b": [1]})
print(rev_idx(["a", "b"]))
print(rev_idx(["a", "B", "A", "aa"]) == {"a": [0, 2], "aa": [3], "b": [1]})
print(rev_idx(["a", "B", "A", "aa"]))
