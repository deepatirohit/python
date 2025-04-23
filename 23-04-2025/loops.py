#  for loop Used to iterate over a sequence like list, string, range, etc.
# in this we will loop over nums and strings

for i in range(5):
    print(i)
    
num = int(input("Enter a number: "))

for i in range(num):
    print(i)

# Print even numbers between 1 and 50

num = 50

for i in range(1, num+1):
    if(i % 2 == 0):
        print(i)

# Print the square of each number from 1 to 5

for i in range(1, 5):
    print(i * i)

# Print each character in a string

text = "python"

for char in text:
    print(char)

# Sum of numbers from 1 to 100

sum = 0

for i in range(1, 100):
    sum += i
print(sum)

# Print multiplication table of any number (e.g., 7)

num = 7
for i in range(1, 11):
    product = num * i
    print(f"{num} * {i} = {product}")

# Print a right-angled triangle pattern using *

num = 5
for i in range(1, num+1):
    print("*" * i)

# Reverse a string using a for loop

text = "python"
reverseStr = ""

for char in text:
    reverseStr = char + reverseStr
print(reverseStr)

# Count vowels in a string

str = "programming"
vowels = ["a", "e", "i", "o", "u"]
count = 0

for char in str:
    if char in vowels:
        count += 1
print(count)

text = "python"


for char in reversed(text):
    print(char)

# A while loop runs as long as a given condition evaluates to True. Once the condition becomes False, the loop will stop.

count = 0

while count <= 5:
    print(count)
    count += 1

# Print numbers from 1 to 10:

num = 1

while num <= 10:
    print(num)
    num += 1

# Print the sum of numbers from 1 to 100

num = 1
sum = 0

while num <= 100:
    sum += num
    num += 1
print(sum)

#  Print a countdown from 10 to 1:

count = 10

while count > 0:
    print(count)
    count -= 1

# Create a while loop to print all odd numbers between 1 and 100

num = 1

while num <= 100:
    if num % 2 == 1:
        print(num)
    num += 1
    
