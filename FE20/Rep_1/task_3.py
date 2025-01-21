def dict_to_lists(d: dict):
    # should return two values: a list of keys in d and a list of corresponding values in d. The sorting does not matter, as long as for each element in the first return value, the corresponding value can be found in the second list under the same index.

    k_lst = []
    v_lst = []

    for i, k in enumerate(d.keys()):
        k_lst.append(k)

    for i, v in enumerate(d.values()):
        v_lst.append(v)

    return k_lst, v_lst


x = {2: "b", 1: "a"}
l1, l2 = dict_to_lists(x)
print(sorted(l1) == [1, 2])
print(sorted(l2) == ["a", "b"])
print(l2[1] == x[l1[1]])
