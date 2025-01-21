def check(speed, limit):
    # If speed is greater than limit, the function should return False, otherwise it should return True. However, if limit is 0, the function should return True whatever the value of speed.

    if limit == 0:
        return True
    if speed > limit:
        return False
    return True


print(check(130, 90))
print(check(170, 0))
