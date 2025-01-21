def reverse(l):

    if not l:
        return []
    else:
        this = l[-1:]
        that = this + reverse(l[:-1])

        return that


print(reverse([]) == [])
print(reverse([2]) == [2])
print(reverse([2, 6, 5]) == [5, 6, 2])

lst = [1, 2, 3, 4, 5]

# print(f"entire {lst[:]}")
# print(f"without last {lst[:-1]}")
# print(f"reverse {lst[::-1]}")
# print(lst[-1:] + [5, 6])
# print(lst[-1 -1:])
# print(lst[])
# print(lst[])
