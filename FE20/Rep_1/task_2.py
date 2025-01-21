def find_both_ways(text: str, word: str):
    # determine if the string word appears in the string text, read either normally or backwards, while ignoring the casing
    # f word appears in text from left to right (i.e. read normally), the function should return the tuple (True, 1). If word appears in text from right to left (i.e. read in reverse), the function should return the tuple (True, -1). If word does not appear, (False, 0) should be returned.

    word = "".join(w.lower() for w in word)
    text = "".join(t.lower() for t in text)

    normal = word
    reverse = word[::-1]

    if normal in text:
        return (True, 1)
    elif reverse in text:
        return (True, -1)
    else:
        return (False, 0)


print(find_both_ways("Hello, World!", "lo, wo") == (True, 1))
print(find_both_ways("Hello, God!", "Dog") == (True, -1))
print(find_both_ways("Hello, California!", "local") == (False, 0))
