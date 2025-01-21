def padded_zip(lists: list, padding=None):
    pass


l1 = [1, 2, 3, 4, 5]
l2 = [1.5, 2.5, 3.5, 4.5]
l3 = ["please", "send", "help"]
# ((1, 1.5, 'please'), (2, 2.5, 'send'), (3, 3.5, 'help'), (4, 4.5, None), (5, None, None))
print(padded_zip([l1, l2, l3]))
# ((1, 1.5, 'please', 1), (2, 2.5, 'send', 2), (3, 3.5, 'help', 3), (4, 4.5, '!', 4), (5, '!', '!', 5))
print(padded_zip([l1, l2, l3, l1], "!"))
