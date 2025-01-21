def strings_containing(strings, word):
    # The function should return a list of strings from strings containing only those strings that contain word (in the original order), ignoring character casing.

    return [s for s in strings if word.lower() in s.lower()]


print(strings_containing(["Hello", "there", "friend"], "he"))
print(strings_containing(["abc", "cde", "DEF"], "de"))
