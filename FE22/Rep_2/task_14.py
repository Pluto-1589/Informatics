

# Solution

def encode(string, offset, salt):
    # convert to ints
    ints = []
    for char in string:
        ints.append(ord(char))
    # apply offset
    shifted = []
    for i in ints:
        shifted.append(i + offset)
    # add salt
    salted = []
    salt_index = 0
    for number in shifted:
        salted.append(number)
        salted.append(salt[salt_index])
        salt_index += 1
        if salt_index == len(salt):
            salt_index = 0
    # back to string
    res = ""
    for i in salted:
        res += chr(i)
    # return steps
    return shifted, salted, res


def decode(string, offset, salt):
    # to shifted ints
    shifted = []
    for char in string:
        shifted.append(ord(char))
    # unsalt
    unsalted = []
    for i, char in enumerate(shifted):
        if i % 2 == 1:
            continue
        unsalted.append(char)
    # un-apply offset
    ints = []
    for i in unsalted:
        ints.append(int(i - offset))
    # back to characters
    res = []
    for i in ints:
        res.append(chr(i))
    # return steps
    return shifted, unsalted, "".join(res)


print(encode("hello", 3, [65, 99, 120]) ==
      ([107, 104, 111, 111, 114], [107, 65, 104, 99, 111, 120, 111, 65, 114, 99], 'kAhcoxoArc'))
print(decode("kAhcoxoArc", 3, [65, 99, 120]) ==
      ([107, 65, 104, 99, 111, 120, 111, 65, 114, 99], [107, 104, 111, 111, 114], 'hello'))
