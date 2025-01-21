

def remove_every(l: list, n: int):

    # Implement a function remove_every which takes two parameters: a list l(containing arbitrary values) and a positive integer n. The function should return a list containing the elements from l but with every n'th element removed. For example, if n is 3, every third element should be removed. You may assume that your function will only be called with parameters that match the given description. Use the following template:

    for i in l:
        if (i + n + 2) % n == 0:
            l.pop(i)
    return l


print(remove_every([1, 2, 3, 4, 5], 2))  # [1, 3, 5]
print(remove_every([1, 2, 3, 4, 5, 4, 3, 2, 1], 3))  # [1, 2, 4, 5, 3, 2]
