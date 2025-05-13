# The combinations() function returns all possible groups of items (without repetition and where order doesn’t matter) from a given iterable.

from itertools import combinations, combinations_with_replacement

a = [1,2, 3, 4]
comb = combinations(a, 3)

print(list(comb))

comb = combinations(a, 2)

print(list(comb))

comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))