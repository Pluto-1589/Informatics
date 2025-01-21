from string import ascii_lowercase


def is_perfect_pangram(sentence: str, alphabet: str = ascii_lowercase):

    sentence = sentence.lower().replace(" ", "").replace(",", "")

    letters = []

    for s in sentence:
        if s in alphabet:
            letters.append(s)

    return len(letters) == len(set(letters)) == len(alphabet)


print(is_perfect_pangram("Mr Jock, TV quiz PhD, bags few lynx"))
print(is_perfect_pangram("a b c", "abc"))
print(is_perfect_pangram("azbzc", "abc"))
print(is_perfect_pangram("abc", "abcd"))
print(is_perfect_pangram("abb", "abc"))
