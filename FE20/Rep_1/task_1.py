def tally(costs: list, discounts: list, rebate_factor: float):
    # subtract the sum of values in discounts from the sum of values in costs and then multiply the result with rebate_factor. Should the result be negative, return 0. The result value should be rounded to 2 decimal places.

    res = round((sum(costs) - sum(discounts)) * rebate_factor, 2)

    if res < 0:
        return 0
    return res


print(tally([10, 24], [3, 4, 3], 0.30) == 7.20)
print(tally([10], [20], 0.1) == 0)
