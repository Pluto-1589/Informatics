def discounted_price(original, low, normal_discount, high, high_discount):

    if original < low:
        return original
    if original >= low and original < high:
        return round(original * normal_discount)
    if original >= high:
        return round(original * high_discount)


print(discounted_price(100, 200, 0.9, 500, 0.7))
print(discounted_price(300, 200, 0.9, 500, 0.7))
print(discounted_price(888, 200, 0.9, 500, 0.7))
