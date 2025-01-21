def all_truthy(values: list):
    # n should determine if all values in values evaluate as True. If yes, it should return True, False otherwise. For an empty list, all values are True.

    if not values:
        return True

    return all(bool(i) == True for i in values)


print(all_truthy([True, "yes", "no", 1, [{}]]))
print(all_truthy([]))
print(not all_truthy([True, "yes", 0.0]))
