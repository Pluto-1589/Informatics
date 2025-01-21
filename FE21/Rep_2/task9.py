def draw(size: int, instructions: list):
    # should use the instructions in instructions to generate and return a string consisting of size lines each having size characters.

    # create empty list
    canvas = []
    # iterate over range of size
    for i in range(size):
        # append empty list to canvas
        canvas.append([])
        # iterate over range of size again
        for j in range(size):
            # list in canvas at index i append " "
            canvas[i].append(" ")

        for tup in instructions:
            x, y, letter = tup
            if x - 1 < len(size):
                raise IndexError
            if y - 1 < len(size):
                raise IndexError
            if len(letter) != 1:
                raise ValueError
            else:
                canvas[j][i] = letter

    lines = ["".join(char) for char in canvas]
    joined_lines = "\n".join(l for l in lines)

    return joined_lines


# DO NOT SUBMIT THE LINES BELOW!
print(draw(1, [(0, 0, "a")]) == "a")
# assert draw(2, [(0, 0, "a"), (1, 1, "b")]) == (
#     "a \n"
#     " b"
# )
# assert draw(3, [(1, 0, "a"), (0, 1, "b")]) == (
#     " a \n"
#     "b  \n"
#     "   "
# )
#
# assert draw(5, [
#  (0, 0, "a"),
#  (1, 2, "a"),
#  (4, 4, "b"),
#  (0, 4, "a"),
#  (1, 1, "a"),
#  (0, 3, "a")]) == (
#    "a    \n"
#    " a   \n"
#    " a   \n"
#    "a    \n"
#    "a   b"
# )
#


# Solution

def draw(size: int, instructions: list):
    # create empty list for results
    canvas = []
    # iterate over the range of size
    for x in range(size):
        # append empty list
        canvas.append([])
        # iterate over the range of size again
        for y in range(size):
            # at the xth list in canvas append " "
            canvas[x].append(" ")
    # iterate over tuples in list
    for i in instructions:
        # split each coordinate and content into different variables
        x, y, c = i
        # check if x and y are out of bound
        if x > size - 1:
            raise IndexError
        if y > size - 1:
            raise IndexError
        # check if len of content is not 1 raise error
        if len(c) != 1:
            raise ValueError
        # at coordinate y x insert c
        canvas[y][x] = c
    # turn individual values into a str in a list comp
    lines = ["".join(chars) for chars in canvas]
    # join using new line
    return "\n".join(lines)
