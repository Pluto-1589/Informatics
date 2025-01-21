def change(pennies: int):

    # value in pennies
    dollars = pennies // 100
    quarters = pennies // 25
    dimes = pennies // 10
    nickels = pennies // 5

    return (dollars, quarters, dimes, nickels)


print(change(162))
print(change(3))
