# functions
# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

def myFunc():
    print("Python functions")

myFunc()

# Arguments
# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

def greet(name):
    print(f"Hello, {name}")

greet("john")
greet("james")
greet("Peter")
greet("Samuel")

# Function with Return:

def sum(a, b):
    return a + b

result = sum(2, 6)
print(result)

# Check Even or Odd
def isEvenOrOdd(num):
    if num %2 == 0:
        return f"{num} is even number"
    else:
        return f"{num} is odd number"

print(isEvenOrOdd(23))
print(isEvenOrOdd(35))
print(isEvenOrOdd(122))
print(isEvenOrOdd(111))
print(isEvenOrOdd(124))

# Count Vowels in a String
text = "Python programming is fun and educational"


def countVowels(text):
    count = 0
    # vowels = ["a", "e", "i", 'o', "u", "A", "E", "I","O", "U"]
    vowels = "aeiou"
    for char in text:
        if char in vowels.lower():
            count += 1
        else:
            pass
    print(count)


countVowels(text)

# Create a function find_max(lst) that returns the largest number in a list.
numbers = [42, 17, 93, 56, 28, 77, 103, 64, 89]

def findMaxNum(numbers):
    maxNum = numbers[0]
    # for i in range(len(numbers)):
    #     if numbers[i] > maxNum:
    #         maxNum = numbers[i]
    
    for num in numbers:
        if num > maxNum:
            maxNum = num
    print(maxNum)

findMaxNum(numbers)

# Reverse a List

my_list = [10, 20, 30, 40, 50]  

def reverseList(my_list):
    result = []
    
    for i in range(len(my_list) - 1, -1, -1):  # Start from last index to 0
        result.append(my_list[i])
        
    print(result)
    
reverseList(my_list)


