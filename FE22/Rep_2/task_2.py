from string import ascii_lowercase


def is_perfect_pangram(sentence: str, alphabet: str = ascii_lowercase):
    # A "pangram" is a word or sentence that uses all letters in an alphabet at least once. A "perfect pangram" uses each letter exactly once.

    # The function is_perfect_pangram should check if sentence is a perfect pangram for the given alphabet. If no alphabet is given, the 26 letters of the English alphabet should be assumed. Character casing and any characters that are not part of the alphabet should be ignored.

    clean_sentence = "".join(s.lower() for s in sentence if s.isalpha())

    res = []

    for char in clean_sentence:
        if char in alphabet:
            res.append(char)

    return len(set(res)) == len(alphabet) == len(res)


print(is_perfect_pangram("Mr Jock, TV quiz PhD, bags few lynx"))  # True
print(is_perfect_pangram("a b c", "abc"))  # True
print(is_perfect_pangram("azbzc", "abc"))  # True
print(is_perfect_pangram("abc", "abcd"))  # False
print(is_perfect_pangram("abb", "abc"))  # False
