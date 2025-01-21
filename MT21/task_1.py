def all_falsy(values):

    if [] in values:
        return True

    f_vals = any(val for val in values if val is False)

    if f_vals is False:
        return True


print(all_falsy([False, "", 0, []]))
print((not all_falsy([False, "no", 0.1])))
print(all_falsy([[]]))

print(all_falsy([False, "", 0, []]))
