def check(speed, limit):
    if limit == 0:
        return True
    elif speed > limit:
        return False
    return True


print(check(130, 90))
print(check(170, 0))
