class BinaryTree:

    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

    def find(self, needle):
        # return a list of all data where needle matched key. More specifically, on a given BinaryTree, find should first compare needle to the tree's key and if it matches, the tree's data should be the first element of the list to be returned. Then, find should call the left and right BinaryTree's find methods recursively, and add their return values to the result to finally return the resulting list.
        if needle:
            if self.left != None:
                return self.find(needle)

        pass


tree = BinaryTree("root", "Tree root",
                  left=BinaryTree("X", "Anna",
                                  left=BinaryTree(123, "Betty",
                                                  left=BinaryTree(
                                                      "C", "Charles"),
                                                  right=BinaryTree(200, "Dora")
                                                  ),
                                  right=BinaryTree("E", "Emil",
                                                   right=BinaryTree(
                                                       200, "Denis")
                                                   )
                                  ),
                  right=BinaryTree(200, "Daniel")
                  )
print(tree.find("X"))
print(tree.find(200))
