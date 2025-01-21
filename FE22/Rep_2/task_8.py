import random
from random import choice


class Coinflips:

    def __init__(self):
        self.guesses = []
        self.actual_flip = []

    def play(self, guess):
        # "heads" or "tails". A Warning should be raised if some other string is passed
        if guess != "heads" or guess != "tails":
            raise Warning
        # play then randomly selects the result of the coin flip for the current round of the game. play should return a string "heads" or "tails" depending on the random result.
        self.guesses.append(guess)
        self.actual_flip.append(choice(["heads", "tails"]))

        return self.actual_flip

    def winner(self):
        # A method winner can be called at any time to determine, whether the player's guesses were correct a majority of the time. winner should return True if the player wins, False otherwise.
        count_correct = 0

        for i in self.guesses:
            if i in self.actual_flip:
                count_correct += 1

        if count_correct > len(self.actual_flip):
            return True
        return False

    def __str__(self):
        return ",".join(self.actual_flip)


t = Coinflips()
try:
    t.play("arms")
except Warning:
    print("invalid choice")  # invalid choice
# Your play results may be different from this example due to randomness
print(t.play("heads"))  # heads
print(t.play("tails"))  # heads
print(t.play("heads"))  # tails
print(t)  # heads, heads, tails
print(t.winner())  # False


# solution


class Coinflips:
    def __init__(self):
        self.__results = []
        self.__choices = []

    def play(self, choice):
        if choice not in ["heads", "tails"]:
            raise Warning
        result = random.choice(["heads", "tails"])
        self.__results.append(result)
        self.__choices.append(choice)
        return result

    def winner(self):
        wins = sum(
            [1 for h, c in zip(self.__results, self.__choices) if h == c])
        losses = len(self.__results) - wins
        return wins > losses

    def __str__(self):
        return ", ".join(self.__results)


# examples
t = Coinflips()
try:
    t.play("arms")
except Warning:
    print("invalid choice")
# Your play results may be different from this example due to randomness
print(t.play("heads"))
print(t.play("tails"))
print(t.play("heads"))
print(t)
print(t.winner())
