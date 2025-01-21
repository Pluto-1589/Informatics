class BinaryTree:
    def __init__(self, key, value=0, left=None, right=None) -> None:
        self.key = key
        self.value = value
        self.left = left
        self.right = right

    def tally(self, needle):
        pass


tree = BinaryTree("root",
                  left=BinaryTree("A",
                                  left=BinaryTree("B", 20,
                                                  left=BinaryTree("C", 60),
                                                  right=BinaryTree("D", -50)
                                                  ),
                                  right=BinaryTree("E",
                                                   right=BinaryTree("D", 70)
                                                   )
                                  ),
                  right=BinaryTree("D", 80)
                  )
print(tree.tally("C"))  # - 0 - 0 - 20 + 60 - -50 - 0 - 70 - 80
print(tree.tally("D"))  # - 0 - 0 - 20 - 60 + -50 - 0 + 70 + 8
