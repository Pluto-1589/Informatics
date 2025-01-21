class BinaryTree:
    def __init__(self, key, data, left=None, right=None) -> None:
        self.key = key
        self.data = data
        self.left = left
        self.right = right

    def find(self, needle):

        if self.left is not None:
            res = self.find(needle) if self.key == needle else self.data
        elif self.right is not None:
            res = self.find(needle) if self.key == needle else self.data
