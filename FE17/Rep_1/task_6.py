class Tree(object):
    def __init__(self, val, left=None, right=None):
        print(type(val) == int)
        assert left == None or type(left) == Tree
        assert right == None or type(right) == Tree
        self.val = val
        self.left = left
        self.right = right


def sumTree(tree):
    # On the next page, implement the function with the signature sumTree(tree) that returns the sum.

    if tree is None:
        return 0
    else:
        return tree.val + sumTree(tree.left) + sumTree(tree.right)


print(sumTree(None) == 0)
print(sumTree(Tree(1)) == 1)
print(sumTree(Tree(1, Tree(2))) == 3)
print(sumTree(Tree(5, Tree(-1), Tree(-2))) == 2)
print(sumTree(Tree(1, Tree(2, Tree(3, Tree(4))))) == 10)
