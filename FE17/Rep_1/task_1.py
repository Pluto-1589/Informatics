def stringify(n: int):
    # The functions should return “«n» is even” if n is an even number, or “«n» is odd” otherwise.
    if n % 2 == 0:
        return f"{n} is even"
    else:
        return f"{n} is odd"


print(stringify(10) == "10 is even")
print(stringify(5) == "5 is odd")
