def discounted_price(original, low, normal_discount, high, high_discount):
    # If original is less than low, the function should return price, rounded to the nearest integer.
    # If original is greater than or equal to low but less than high, the function should return original multiplied by normal_discount, rounded to the nearest integer.
    # If original is greater than or equal to high, the function should return original multiplied by high_discount, rounded to the nearest integer.

    if original < low:
        return round(original)
    elif original >= low and original < high:
        return round(original*normal_discount)
    elif original >= high:
        return round(original * high_discount)


print(discounted_price(100, 200, 0.9, 500, 0.7))
print(discounted_price(300, 200, 0.9, 500, 0.7))
print(discounted_price(888, 200, 0.9, 500, 0.7))
