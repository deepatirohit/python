import copy


# immutable types
org = 5
cpy = org
cpy = 6

print(cpy)
print(org)

#mutable types
org_list = [0, 1, 2, 3, 4, 5, 6, 7]
copy_list = org_list
copy_list[0] = -10

print(copy_list)
print(org_list)

# copying using copy module
org = [0, 1, 2, 3, 4, 5]
copy_list = copy.copy(org)
copy_list[0] = 20

print("Original list: ", org)
print("copy list: ", copy_list)

org = [0, 1, 2, 3, 4, 5]
copy_list = list(org)
copy_list[0] = 20

print("Original list: ", org)
print("copy list: ", copy_list)

org = [0, 1, 2, 3, 4, 5]
copy_list = org[:]
copy_list[0] = 20

print("Original list: ", org)
print("copy list: ", copy_list)

# shallow copy

org = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
cpy = copy.copy(org)
cpy[0][0] = -10
print("copy list", cpy)
print(org)

# deep copy
org = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
cpy = copy.deepcopy(org)
cpy[0][0] = -10
print("copy list", cpy)
print(org)