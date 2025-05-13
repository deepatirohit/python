# collections: Counter

from collections import Counter
text = "aaaaaaaaaabbbbbvvvccccccddd"
my_counter = Counter(text)
print(my_counter)

print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())
print(my_counter.most_common(3))
print(my_counter.most_common(1)[0][0])
print(list(my_counter.elements()))