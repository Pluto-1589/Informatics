def to_list(thing, transform=lambda x: [x]):
    # the function to_list should attempt to call Python's built-in list function with thing as the argument and return the result. If this fails because of any exception, to_list should instead return the value resulting from calling transform with thing as the parameter. By default, transform should simply return a list containing the value passed to it as the only element.

    try:
        return list(thing)
    except:
        return transform(thing)


print(to_list([1, 2, 3]))
print(to_list((1, 2, 3)))
print(to_list(1.5))
print(to_list(True))
print(to_list(True, lambda x: [int(x)]))
