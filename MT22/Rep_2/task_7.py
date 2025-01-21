import random
# this line of code makes it so that calls to random always produce the same
# successive values so that the examples below always produce the same results
random.seed(7)


def lottery(limit, guess, prize):
    # draw n unique random numbers in the range from (and including) 1 to (and including) limit. n is implied by the length of the guess provided by the player.

    draws = []

    for i in range(1, limit + 1):
        i = random.randint()
        draws.append(i)

    # check how many numbers in guess appear in the random draw
    count = 0
    for i in draws:
        if i in guess:
            count += 1

    # calculate the payout according to the following rule: For an exact match, the whole prize is paid out. If one number differs, half of the prize is paid out. If two numbers differ, a quarter of the prize is paid out, and so on. If none of the numbers match, the prize money is 0.
    dif_count = 0
    for i, v in enumerate(draws):
        for x, y in enumerate(guess):
            if draws[i] == v != guess[i] == y:
                dif_count += 1
            if dif_count == 0:
                prize = prize
            elif dif_count == 1:
                prize = prize * 0.5
            elif dif_count == 2:
                prize = prize * 0.25
            else:
                prize = 0

    return (draws, dif_count, prize)


print(lottery(52, [4, 8, 15, 16, 23, 42], 1000000))  # 2 matching
print(lottery(3, [1, 2, 3], 1000000))               # inevitable perfect match
# zero matchingimport random
print(lottery(10000, [1, 2, 3], 1000000))
