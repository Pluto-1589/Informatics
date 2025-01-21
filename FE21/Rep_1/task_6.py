# COULDNT SOLVE YET

# Implement a function intersperse, which takes two parameters: a non-empty string s and a non-empty list of strings l. The function should return the string s while the elements from l should be inserted one by one in-between the characters in s. Once the last element in l has been inserted, the selection should return to the beginning. Consider the assertions given below as examples for using intersperse.

def intersperse(s: str, l: list):
    # res is string at position zero
    res = s[0]
    # set deliminator to 0
    delim = 0
    # loop over string starting at the first position
    for c in s[1:]:
        # res is updated to list item at position deliminator modular the length of the list:
        # so delim = 0 and len is 2 -> 0 % 2 = 0 or 9 % 2 = 1
        res += l[delim % len(l)]
        # add c to res
        res += c
        delim += 1
    return res


    # DO NOT SUBMIT THE LINES BELOW!
# print(intersperse("H", [',']) == "H")
print(intersperse("Hello", [',']) == "H,e,l,l,o")
# print(intersperse("Hello", [',', '.']) == "H,e.l,l.o")
# print(intersperse("Hello", ['', '.']) == "He.ll.o")
# print(intersperse("Hello", ['-o-', '_o_']) == "H-o-e_o_l-o-l_o_o")
# print(intersperse("Hello", [',', '.', '-']) == "H,e.l-l,o")
