def count_characters(text):
    from collections import Counter

    return dict(Counter(text))


print(count_characters("hello"))
print(count_characters("Прогресс"))
print(count_characters("<3"))
print(count_characters(""))
