def calc(expression):

    operator, num_1, num_2 = expression.split()

    num_1 = float(num_1)
    num_2 = float(num_2)

    if num_1 == 0 or num_2 == 0:
        raise ValueError("Cannot divide by 0")

    if operator == "+":
        return num_1 + num_2
    elif operator == "-":
        return num_1 - num_2
    elif operator == "*":
        return num_1 * num_2
    elif operator == "/":
        return num_1 / num_2


# DO NOT SUBMIT THE LINES BELOW!
print(calc("+ 1 2"))  # == 3)
print(calc("- 1 2") == -1)
print(calc("* 1 2") == 2)
print(calc("/ 1 2") == 0.5)
print(calc("* 1 -2") == -2)
print(calc("* 10.5 2") == 21)
print(calc("* -10.5 -2") == 21)
