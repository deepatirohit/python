# multiplication
result = 2 * 5
print(result)


# power operation
result = 2 ** 5
print(result)

result = 2**2
print(result)

# list operator
zeros = [0] * 10
print(zeros)

numbers = [1, 2, 3] * 5
print(numbers)

# tuple operator
mytuple = (1, 2, 3, 4) * 4
print(mytuple)

# string 
mystring = "abc" * 5
print(mystring)

# we will use * in *args and *kwargs in function parameters 

# unpacklist
numbers = [1, 2, 3, 4, 5, 6, 7]
*beginning, last = numbers

print(beginning)
print(last)

tupleNumbers = [1, 2, 3, 4, 5, 6, 7]
*beginning, last = tupleNumbers

print(beginning)
print(last)

numbers = [1, 2, 3, 4, 5, 6, 7]
beginning, *last = numbers

print(beginning)
print(last)

numbers = [1, 2, 3, 4, 5, 6, 7]
beginning, *middle, last = numbers

print(beginning)
print(middle)
print(last)