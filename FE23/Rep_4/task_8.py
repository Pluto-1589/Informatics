class StringDict:

    def __init__(self, elements=None):
        self.elements = {}

        if elements:
            for k, v in self.elements.items():
                self.elements[k] = str(v)

    def __len__(self):
        return len(self.elements)

    def __eq__(self, other):
        return self.elements == other.elements

    def __setitem__(self, key, value):
        self.elements[key] = str(value)

    def __getitem__(self, key):
        return self.elements[key]

    def __repr__(self):
        return repr(self.elements)

    def __str__(self):
        return str(self.elements)

    def __contains__(self, thing):
        return thing in self.elements


    # setting a value via the bracket notation: d[key] = value
    # retrieving a value via the bracket notation: d[key]
    # printing: print(d), which should appear the same way as when printing a regular dictionary
    # printing in a collection: print([d]), which should appear the same way as when printing a regular dictionary in a collection
    # getting its size: len(d)
    # the in operator: 123 in d, which, just like with regular dictionaries, checks if a key is present in the StringDict
    # equality: d1 == d2 and d1 != d2
    # providing an optional, regular dictionary upon instantiation; don't forget to convert the values to strings.
d1 = StringDict()
print(d1)  # {}
d1[1] = 100
d1["abc"] = print
print(d1)  # {1: '100', 'abc': '<built-in function print>'}
print(isinstance(d1[1], str))  # True
print(1 in d1)  # True
print(100 in d1)  # False
print(len(d1))  # 2
d2 = StringDict({"abc": print, 1: "100"})
d3 = StringDict({"abc": max})
print(d1 == d2)  # True
print(d1 == d3)  # False


# Solutions

class StringDict:

    # takes something but is set to none in case no arguments are given
    def __init__(self, elements=None):
        # elements are empty dict by default
        self.__elements = {}
        # if elements not none convert value to string
        if elements:
            for k, v in elements.items():
                self.__elements[k] = str(v)

    def __len__(self):
        return len(self.__elements)

    def __eq__(self, other):
        return self.__elements == other.__elements

    def __setitem__(self, key, value):
        self.__elements[key] = str(value)

    def __getitem__(self, key):
        return self.__elements[key]

    def __str__(self):
        return str(self.__elements)

    def __repr__(self):
        return repr(self.__elements)

    def __contains__(self, thing):
        return thing in self.__elements

# or simply:


class StringDict(dict):
    def __init__(self, elements=None):
        if elements:
            for k, v in elements.items():
                elements[k] = str(v)
            super().__init__(elements)
        else:
            super().__init__()

    def __setitem__(self, key, value):
        super().__setitem__(key, str(value))
