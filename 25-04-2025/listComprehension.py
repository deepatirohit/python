# list comprehension = a concise way to create lists in python
# compact and easier to read than traditional loops
# [expression for value in iterables if condition]


# traditional loop
doubles = []
for x in range(1, 11):
    doubles.append(x * 2)

print(doubles)

# list comprehension

# doubles =[expression for value in iterables if condition]
doubles = [x * 2 for x in range(1, 11)]
print(doubles)

triples = [num * 3 for num in range(1, 11)]
print(triples)

# square of each number:
square = [num * num for num in range(1, 11)]
print(square)

fruits = ["apple", 'orange', "banana", "coconut"]

fruits = [fruit.upper() for fruit in fruits]
print(fruits)

fruits = [fruit.upper() for fruit in ["apple", 'orange', "banana", "coconut"]]
print(fruits)

fruits = ["apple", 'orange', "banana", "coconut"]

fruit_char = [fruit[0] for fruit in fruits]
print(fruit_char)

numbers = [-10, -5, 0, 3, 7, -2, 8, -15, 20, -1, 12]

postiveNumbers = [num for num in numbers if num >= 0]
print(postiveNumbers)

negativeNumbers = [num for num in numbers if num < 0]
print(negativeNumbers)

evenNums = [num for num in numbers if num % 2 == 0]
print(evenNums)

oddNums = [num for num in numbers if num % 2 == 1]
print(oddNums)

grades = [85, 42, 79, 90, 56, 61, 30]

passingGrades = [grade for grade in grades if grade >= 60]

print(passingGrades) 