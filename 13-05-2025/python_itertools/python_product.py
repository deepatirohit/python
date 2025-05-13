from itertools import product

a = [1,2,3,4,5]
b = [6,7,8,9]

prod = product(a, b)
print(prod)
print(list(prod))

prod = product(a, b, repeat=2)
print(list(prod))