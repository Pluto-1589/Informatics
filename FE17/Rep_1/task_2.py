def compute_stats(lst):

    ordered_lst = sorted(lst)

    sec_highest = ordered_lst[-2]
    average = sum(lst) / len(lst)
    if len(stats) % 2 != 0:
        half_size = len(ordered_lst) // 2
        median = ordered_lst[half_size]

    return (sec_highest, average, median)


stats = [1, 12, 4, 5, 8]

stats = compute_stats(stats)
print(stats[0] == 8 and stats[1] == 6 and stats[2] == 5)

a = [11.20, 5.90]
print(compute_stats(a))
# print(stats([0] == 5.90 and stats[1] == ] and stats[2] == 5.90))
