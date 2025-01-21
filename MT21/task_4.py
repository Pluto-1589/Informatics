def greetings(names):

    if not names:
        return "Hello?"
    else:
        almost_all_names = names[:-1]
        almost_all_names = ", ".join(almost_all_names)
        last_name = names[-1]
        last_name = "".join(last_name)
        if len(names) == 1:
            names = "".join(names)
            return f"Hello {names}."
        return f"Hello {almost_all_names} and {last_name}."


print(greetings([]))
print(greetings(['Josh']))
print(greetings(['Josh', 'Alice']))
print(greetings(['Josh', 'Alice', 'Marie']))


# Carol's way:
def greetings(names):
    # For this task we assume names is always a non-null list.

    g = 'Hello?'
    # if names truthy
    if names:
        # reassign g to hello concatenated to the joined str of the names with ,  up to the second last item
        g = 'Hello ' + ', '.join(names[:-1])
        # to that concatenate and if length of names list if greater than 1  else nothing
        g += ' and ' if len(names) > 1 else ''
        # to that add last name in list
        g += f"{names[-1]}."
    return g
