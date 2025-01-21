import string


def count_palindromes(sentence: str):
    # The function should return the number of palindromes in sentence as an integer. A palindrome is a word that can be read the same forwards and backwards. A palindrome must be at least 3 characters long. The function should be case-insensitive and ignore special characters in words. Consider the assertions given below as examples for using count_palindromes.

    words = sentence.split()

    count = 0

    for word in words:
        if len(word) > 1:
            for letter in word:
                if letter in string.punctuation:
                    word = word.replace(letter, "")
            word = word.lower()
            if word[:] == word[::-1]:
                count += 1
        else:
            False

    return count


# DO NOT SUBMIT THE LINES BELOW!
print(count_palindromes("Having fun!") == 0)
print(count_palindromes("Bob and otto") == 2)
print(count_palindromes("Where's Dad?") == 1)
print(count_palindromes("Otto is my dad.") == 2)
print(count_palindromes("I don't like pop music") == 1)


# Carol's solution

def count_palindromes(sentence):
    tokens = sentence.split()
    res = 0
    for t in tokens:
        t = "".join([c for c in t if c.isalpha()])
        if len(t) < 3:
            continue
        if t.lower() == t[::-1].lower():
            res += 1
    return res
