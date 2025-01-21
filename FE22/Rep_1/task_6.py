class Order:

    def __init__(self, items: list, cost: float) -> None:
        self.items = items
        self.cost = cost

    def __eq__(self, other: object) -> bool:
        # Two instances of Order are equal if and only if the list of items contains the same strings and if the cost is the same.

        if not isinstance(other, Order):
            return NotImplemented

        self.items.sort()
        other.items.sort()

        return self.items == other.items and self.cost == other.cost


print(Order(["Beer", "Wine", "Beer"], 14.50) ==
      Order(["Wine", "Beer", "Beer"], 14.50))
print(Order(["Beer", "Wine", "Beer"], 14.50) != Order(["Wine", "Beer"], 14.50))
print(Order(["Beer", "Pretzels"], 14.50) == "Healthy meal")


# Actual result, where in the instructions was it mentioned that they should be private attributes????

# class Order:
#     def __init__(self, items, cost):
#         self.__items = items
#         self.__cost = cost

#     def __eq__(self, other):
#         if not isinstance(other, Order):
#             return NotImplemented
#         return sorted(self.__items) == sorted(other.__items) and self.__cost == other.__cost

# # examples
# print( Order(["Beer", "Wine", "Beer"], 14.50) == Order(["Wine", "Beer", "Beer"], 14.50) )
# print( Order(["Beer", "Wine", "Beer"], 14.50) != Order(["Wine", "Beer"], 14.50) )
# print( Order(["Beer", "Pretzels"], 14.50) == "Healthy meal" )
