def hailstone(n: int):
    # if the current element is even, divide it by 2 to generate the next element

    res = [n]

    while n != 1:
        if n % 2 == 0:
            n = n // 2
            res.append(n)
        else:
            n = n * 3 + 1
            res.append(n)

    return res


print(hailstone(1) == [1])
print(hailstone(3) == [3, 10, 5, 16, 8, 4, 2, 1])
print(hailstone(7) == [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, ...])
print(hailstone(7))
