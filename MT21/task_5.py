def is_sub_collection(a, b):

    if not b:
        return True

    a = set(a)
    b = set(b)

    if not b.intersection(a):
        return False
    else:
        return True


print(is_sub_collection([], []))
print(not is_sub_collection([], [True]))
print(is_sub_collection([1, 2, 3, None], [None]))


# Carol's solution:
def is_sub_collection(a, b):
    # For this task we assume a b are always non-null lists.
    for i in b:
        if i not in a:
            return False
    return True
