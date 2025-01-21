from collections import Counter
from string import punctuation


def is_isogram(sentence):
    # An isogram is a sequence of characters, where every letter appears the same number of times. If sentence is an isogram, the function should return True, False otherwise. The function should be case-insensitive and ignore special characters. If sentence is not a String, a TypeError should be raised. If sentence is the empty string or contains only special characters, a ValueError should be raised. Consider the assertions given below as examples for using is_isogram.

    if not isinstance(sentence, str):
        raise TypeError

    if sentence == "":
        raise ValueError

    if all(s for s in sentence in punctuation):
        raise ValueError

    res = Counter(sentence)

    for k, v in res:
        k.lower()

    res = {k: v for k, v in res.items() if k.isalpha() and v == v[0]}

    if res:
        return True


# DO NOT SUBMIT THE LINES BELOW!
print(is_isogram("uncopyrightable"))
print(is_isogram("The big dwarf only jumps."))
print(is_isogram("Apple-ale"))
print((not is_isogram("bass")))
print((not is_isogram("Tart")))
