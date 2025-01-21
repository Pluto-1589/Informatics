from re import findall


def spliter(text):

    if not text:
        return []

    if " " not in text:
        return [text]
    else:
        res = findall(r"[a-zA-Z]+", text)

    return res


print(spliter("") == [])
print(spliter("aaa") == ["aaa"])
print(spliter("aaa"))
print(spliter("a bbb cc") == ["a", "bbb", "cc"])
print(spliter("a bbb cc"))
print(spliter("a absf iew isjd"))


def spliter_easy(text):
    return text.split()


print(spliter_easy("") == [])
print(spliter_easy("aaa") == ["aaa"])
print(spliter_easy("aaa"))
print(spliter_easy("a bbb cc") == ["a", "bbb", "cc"])
print(spliter_easy("a bbb cc"))
print(spliter_easy("a absf iew isjd"))
