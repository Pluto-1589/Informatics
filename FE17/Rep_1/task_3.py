def count_letters(s):
    # counts the occurrences of upper and lower case letters in a string. The return value is a dictionary that contains the respective values through the keys upper and lower

    d = {}

    if not isinstance(s, str):
        return False

    upper_count = 0
    lower_count = 0

    for i in s:
        if i.isupper():
            upper_count += 1
        elif i.islower():
            lower_count += 1

    d["upper"] = upper_count
    d["lower"] = lower_count

    return d


d = d = count_letters("Abc Defg HiJ!")

print(d["upper"] == 4 and d["lower"] == 6)
