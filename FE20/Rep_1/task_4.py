def is_divisible_by(n: int, numbers: list):
    # should determine if n is divisible by all numbers in numbers, in which case it should return True. If not, the function should return False. If numbers is empty or includes 0, the function should raise a ValueError.

    if not numbers or 0 in numbers:
        raise ValueError

    if all(n % num == 0 for num in numbers):
        return True
    return False


print(is_divisible_by(30, [3, 6, 15]))
print(not is_divisible_by(30, [3, 6, 29]))
try:
    is_divisible_by(30, [0, 6, 29])
    print(False)  # expected an exception!
except ValueError:
    pass  # the correct exception was thrown
