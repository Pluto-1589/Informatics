def mirror(s):
    # Implement a function that mirrors a string, i.e., it takes the string and adds its reversed form. The last letter should not be duplicated

    if len(s) == 1:
        return s

    middle = len(s) // 2
    reverse = s[::-1]

    res = s[:middle + 1] + reverse[middle - 1:]

    return res


print(mirror("hello"))  # abcba


def mirror_string(s):
    # Reverse the string and remove the last character
    # Slicing to remove the last character of the reversed string
    reversed_part = s[-2::-1]
    # Concatenate the original string with the modified reversed part
    return s + reversed_part


print(mirror_string("abc"))  # abcba
