# 2D colletion of list
# A 2D list is a type of list where each element is itself a list.
# It is used to store data in rows and columns, just like a table or a matrix.

fruits = ["apple", "banana", "orange", "coconut"]
vegetables = ["tamato", "brinjal", "carrots", "potatos"]
meats = ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]
# print(groceries)

fruits[0] = "pineapple"
print(fruits)
print(vegetables)
print(meats)

print(groceries)
print(groceries[0])
print(groceries[1])
print(groceries[2])

print(groceries[0][0])
print(groceries[0][1])
print(groceries[0][2])

print(groceries[1][0])
print(groceries[1][1])
print(groceries[1][2])


print(groceries[2][0])
print(groceries[2][1])
print(groceries[2][2])


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# 👉 Print the matrix row by row

print(matrix[0])
print(matrix[1])
print(matrix[2])

# Print the element in the 2nd row, 3rd column.
print(matrix[1][2])

# Print the element in the 1st row, 1st column.
print(matrix[0][0])

# Calculate the sum of all numbers in a 3x3 matrix.
total = 0

for row in matrix:
    for num in row:
        total += num

print(total)

# Write a program to count even and odd numbers in a 2D list.

evenCount = 0
oddCount = 0
for row in matrix:
    for num in row:
        if num %2 == 0:
            evenCount += 1
        else:
            oddCount += 1

print(evenCount)

print(oddCount)

# 2d collections using tuples

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9))

print(num_pad)

for row in num_pad:
    for num in row:
        print(num, end=" ")