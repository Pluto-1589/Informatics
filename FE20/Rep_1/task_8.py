from collections import Counter


def are_anagrams(a, b):
    # If two character sequences contain the same number of the same corresponding letters, these words are anagrams. Examples: "evil" and "vile", "Eleven plus two" and "Twelve plus one", "A BB CCC" and "cccbba".

    # The function should determine if a and b are anagrams and return True if yes, otherwise False. Non-alphanumerical symbols as well as casing should both be ignored.

    # case insensitive
    a = "".join(l.lower() for l in a)
    b = "".join(l.lower() for l in b)

    # remove nonalpha chars
    a = "".join(l for l in a if l.isalpha())
    b = "".join(l for l in b if l.isalpha())

    a_dict = dict(Counter(a))
    b_dict = dict(Counter(b))

    if a_dict == b_dict:
        return True
    return False


print(are_anagrams('Dog', 'God'))
print(are_anagrams("The Meaning of Life.", "The fine game of nil!"))
print(not are_anagrams("The Meaning of Life", "Work"))
