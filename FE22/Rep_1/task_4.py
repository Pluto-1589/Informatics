class Hand:

    def __init__(self, cards: list) -> None:
        self.cards = cards

        if 1 in self.cards:
            self.cards.append(10)

    def __eq__(self, other: list) -> bool:
        # Two instances of Hand are equal if the sum of card values is the same for both instances.

        if not isinstance(other, Hand):
            return NotImplemented

        return sum(self.cards) == sum(other.cards)


print(Hand([1, 2]) == Hand([10, 3]))
print(Hand([2, 5, 7]) == Hand([10, 4]))
print(Hand([2, 5, 7]) != Hand([9]))
print(Hand([2, 5, 7]) == "Flush")
