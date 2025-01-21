def classify(name, age, child, adult, senior):
    # If age is less than child, the function should return "NAME is an infant".
    # If age is greater than or equal to child but less than adult, the function should return "NAME is a child".
    # If age is greater than or equal to adult but less than senior, the function should return "NAME is an adult".
    # If age is greater than or equal to senior, the function should return "NAME is a senior".

    if age < child:
        return f"{name} is an infant"
    if age >= child and age < adult:
        return f"{name} is a child"
    if age >= adult and age < senior:
        return f"{name} is an adult"
    if age >= senior:
        return f"{name} is a senior"


print(classify("Bobby", 4,  5, 18, 65))
print(classify("Bobby", 5,  5, 18, 65))
print(classify("Bobby", 25, 5, 18, 65))
print(classify("Bobby", 70, 5, 18, 65))
