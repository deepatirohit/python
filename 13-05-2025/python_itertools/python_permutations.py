from itertools import permutations

# It returns all possible arrangements (order matters) of a given iterable's elements, of a specified length.
a = [1, 2, 3, 4, 5]
perm = permutations(a)
print(list(perm))

perm =  permutations(a, 2)
print(list(perm))