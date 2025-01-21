def recursive_join(delim: str, values: list):
    # The function should join the values in values using delim as the delimiter and return the result.

    if len(values) == 1:
        return values[0]
    else:
        this = values[0] + delim
        that = recursive_join(delim, values[1:])

        return this + that


print(recursive_join(" ", ["Hello", "world"]) == "Hello world")
print(recursive_join(" <o> ", ["a", "b", "c"]) == "a <o> b <o> c")
print(recursive_join("", ["a", "b", "c"]) == "abc")
print("Your solution must be recursive!")
