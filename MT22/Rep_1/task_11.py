def sort_dict_values(d: dict):

    for i in d:
        if not d[i]:
            return []
        else:
            d[i] = sorted(d[i])
        return d


print(sort_dict_values({"a": [3, 1, 2]}))  # {'a': [1, 2, 3]}
print(sort_dict_values({1: ["z", "az"], 2: [1]}))  # {1: ['az', 'z'], 2: [1]}


# The sir's solution:

def sort_dict_values(d):

    res = {}
    for key, value in d.items():
        res[key] = sorted(value)

    return res

# a tad mor elegant than mine if i may say
