def censor(text: str, censored_words: list):
    # split the string text into list of words
    words = text.split()
    # create empty list
    res = []
    # For every word in words, check if the word (lower case and without non-alphabetical characters) appears in censored_words.
    # If not, add the unchanged word (i.e. with original casing and non-alphabetical characters) to res.
    # If yes, replace all alphabetical characters with "#" (leaving other characters unchanged) and add the result to res.

    # iterate over each word in words list
    for word in words:
        # condition the word str so its all alpha and lowercase
        # join comprehension char for char in word if char is alpha then lower it
        stripped_word = "".join([c for c in word if c.isalpha()]).lower()
        # check if the stripped word is in censored words
        if stripped_word in censored_words:
            # if so join # if the char is alpha else join the letters in the word
            censored_word = "".join("#" if c.isalpha() else c for c in word)
            # add to results
            res.append(censored_word)
        else:
            # add word to results if stripped word wasnt found in censored words
            res.append(word)
    # join each list item into a str
    return " ".join(res)


print(censor("Hello, World!", ["hello"])
      == "#####, World!")
print(censor("Everything is going to be fine!", ["everything", "fine"])
      == "########## is going to be ####!")
print(censor("", ["does", "not", "matter"])
      == "")
print(censor("Everything is going to be fine!", [])
      == "Everything is going to be fine!")
