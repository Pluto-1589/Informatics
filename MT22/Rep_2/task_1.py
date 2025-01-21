def normalize(number, lower, upper):
    # If number is smaller than lower, the function should return lower. If number is larger than upper, it should return upper. Otherwise, the function should return number.

    if number < lower:
        return lower
    elif number > upper:
        return upper
    return number


print(normalize(1.5, 0, 1))
print(normalize(15, 10, 20))
