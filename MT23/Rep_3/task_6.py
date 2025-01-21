def venn(one, two, three):
    # The function should return a set containing all those unique values which appear in both l1 and l2 at least once but which do not appear in l3.
    one = set(one)
    two = set(two)
    three = set(three)

    return (one).union(two).intersection(three)


print(venn([1, 2, 2, 2, 3, 4], [2, 2, 3, 4], [3]))
print(venn([1.0, "hi", 3], [1.0, 3, "hi"], [3, 1]))
print(venn([1, 2, 3], [4, 5, 6], []))
print(venn([1, 2, 3], [1, 2, 3], [1, 2, 3]))
