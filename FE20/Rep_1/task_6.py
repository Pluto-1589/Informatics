import random


def lottery(values: list):
    # The function should now determine, how many values of draw are also in values. The function should return two values: first, draw and second, the number of matching values.
    draw = random.sample(range(1, 51), k=len(values))
    # complete the implementation of this function

    count = 0

    for i in draw:
        if i in values:
            count += 1

    return (draw, count)


guess = [1, 2, 3, 4, 5]
res = lottery(guess)
print(len(res[0]) == len(guess))
print(res[1] in range(0, len(guess)+1))
