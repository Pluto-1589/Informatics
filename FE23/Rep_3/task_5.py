class BinaryTree:

    def __init__(self, key, value=0, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

    def tally(self, needle):
        # tally should recursively traverse the BinaryTree data structure and eventually return a kind-of-sum of all values in the tree, adding those values where needle matches key, and subtracting all others. Besides comparing needle to the tree's key, tally will also need to call the left and right BinaryTree's tally methods recursively to add their return values to the result.

        # res is value added if key equivalent to needle otherwise subtract value
        res = self.value if self.key == needle else -self.value
        # if left node is not none
        if self.left != None:
            # add left node after being tallied over needle to res
            res += self.left.tally(needle)
        # if right node is not none
        if self.right != None:
            # add right node after being tallied over needle to res
            res += self.right.tally(needle)
        return res


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
print(tree.tally("D"))  # - 0 - 0 - 20 - 60 + -50 - 0 + 70 + 80
