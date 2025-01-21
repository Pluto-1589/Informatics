class Hand:

    def __init__(self, cards):
        self.cards = cards

    def __eq__(self, other):
        # Two instances of Hand are equal if the sum of card values is the same for both instances. However, in this game, the card with value 1 counts as 11 for the equality operation. Considering the first example below, the sum of cards 1 and 2 is 13 because the 1 counts as 11.

        if not isinstance(other, Hand):
            return NotImplemented
        else:
            if 1 in self.cards:
                hand_a = sum(self.cards) + 10
            else:
                hand_a = sum(self.cards)

            if 1 in other.cards:
                hand_b = sum(other.cards) + 10
            else:
                hand_b = sum(other.cards)

        return hand_a == hand_b


print(Hand([1, 2]) == Hand([10, 3]))
print(Hand([2, 5, 7]) == Hand([10, 4]))
print(Hand([2, 5, 7]) != Hand([9]))
print(Hand([2, 5, 7]) == "Flush")


# Solutions

class Hand:
    def __init__(self, cards):
        self.__cards = cards

    def __eq__(self, other):
        if not isinstance(other, Hand):
            return NotImplemented
        this = sum(self.__cards)
        that = sum(other.__cards)
        if 1 in self.__cards:
            this += 10
        if 1 in other.__cards:
            that += 10
        return this == that
