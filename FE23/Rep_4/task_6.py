class BinaryTree:

    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

    def find(self, needle):

        res = []

        if self.key == needle:
            res.append(self.data)

        if self.left:
            res.extend(self.left.find(needle))

        if self.right:
            res.extend(self.right.find(needle))

        return res


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
