# list - Lists are used to store multiple items in a single variable.


mylist = ["apple", "banana", "cherry", 34, 3.14]

print(mylist)

# list methods
# append()	Adds an element at the end of the list

mylist = ["apple", "banana", "cherry", 34, 3.14]

mylist.append("orange")
mylist.append(24)

mylist2 = ["ford", "BMW", "vovlo"]
mylist.append(mylist2)

print(mylist)

# clear()	Removes all the elements from the list

mylist = ["apple", "banana", "cherry", 34, 3.14]
mylist.clear()
print(mylist)

# copy()	Returns a copy of the list
mylist = ["apple", "banana", "cherry", 34, 3.14]
copyList = mylist.copy()

print(copyList)

# count()	Returns the number of elements with the specified value

mylist = ["apple", "banana", "cherry", 34, 3.14, 34, "cherry"]

print(mylist.count(34))
print(mylist.count("cherry"))

# extend()	Add the elements of a list (or any iterable), to the end of the current list

fruits = ["apple", "banana", "cherry"]
cars = ["audi", "tata", "honda"]
fruits.extend(cars)

print(fruits)

# index()	Returns the index of the first element with the specified value

fruits = ['apple', 'banana', 'cherry', 'mango', 'orange', 'apple', 'banana', 'cherry', 'mango', 'orange']

print(fruits.index("mango"))
print(fruits.index("orange"))
print(fruits.index("apple"))

# insert()	Adds an element at the specified position

names = ["james", "john", "peter", "marry", "gary", "sophia", "thomas"]

names.insert(3, "sharma")
names.insert(2, "samuel")
names.insert(20, "teju")

print(names)

# pop()	Removes the last item in the list
names = ["james","bob", "john", "peter", "marry", "gary", "sophia", "thomas",  "alex"]

print(names.pop())
names.reverse()
names.sort()

print(names)

# Add 5 different elements (both strings and numbers) to an empty list and print it.

mylist1 = []
mylist1.append("state")
mylist1.append("city")
mylist1.append(35)
mylist1.append(23.98)
mylist1.append("village")

print(mylist1)

# Create a list with 5 items, then clear it and print the result.
mylist = ["cat", "dog", "fish", "parrot", "lion"]
mylist.clear()
print(mylist)

# Copy a list of names and change one item in the copied list. Check if the original list is affected.

names = ["ram", "sam", "rahul", "teja"]
copiedNames = names.copy()
copiedNames.pop()

print(f"copied names: {copiedNames}")
print(f"original Names: {names}")

# Count how many times a number or fruit appears in a list.
items = ["apple", "banana", "apple", "cherry", "banana", "apple"]
appleCount = items.count("apple")
bananeCount = items.count("banana")
cherryCount = items.count("cherry")

print(f"apple count: {appleCount}")
print(f"banana count: {bananeCount}")
print(f"cherry count: {cherryCount}")

# Combine two lists: one with fruits and another with vegetables.


fruits = ["mango", "grapes", "cherry", "banana", "orange"]
veggies = ["carrot", "potato", "brinjal", "carrot"]
fruits.extend(veggies)
veggies.extend(fruits)
print(fruits)
print(veggies)


colors = ["red", "green", "blue", "yellow", "green"]

print(colors.index("red"))
print(colors.index("green"))
print(colors.index("blue"))
print(colors.index("yellow"))

# Insert 3 names at different positions (start, middle, end) in a list.
import math
people = ["sam", "john", "teja"]

start = 0
end  =  len(people)
middle = math.floor((start + end))//2
people.insert(0, "john")
people.insert(middle, "james")
people.insert(len(people), "peter")

print(people)

# Remove the last two items from a list using pop() and print each removed item.

animals = ["dog", "cat", "lion", "tiger", "elephant"]

animals.pop()
animals.pop()

for animal in animals:
    print(animal)

# Remove a specific item (by value) from the list.

places = ["delhi", "mumbai", "chennai", "kolkata"]
places.remove("chennai")
print(places)

#  Reverse the order of a list and print it.
nums = [1, 2, 3, 4, 5]
nums.reverse()
print(nums)

friends = ["teju", "balu", "anil", "zara"]
friends.sort()
print(friends)

# Given a list of numbers, split them into two lists: one for even numbers and one for odd numbers.

nums = [1,2,3,4,5,6,7,7,8,8,9,10,112,14,33,64,75,23,753,43]
evenNums = []
oddNums = []

for num in nums:
    if(num % 2 == 0):
        evenNums.append(num)
    else:
        oddNums.append(num)

print(f"Even numbers list: {evenNums}")
print(f"Odd numbers list: {oddNums}")

# Write a program to calculate the sum and average of all numbers in a list.

list = [1,2,3,4,5,6,7,7,8,8,9,10,112,14,33,64,75,23,753,43]

sum = 0


for i in list:
    sum += i
print(sum)

average = sum / len(list)

print(average)

# method 2

sum = 0

for i in range(len(list)):
    sum += list[i]
print(sum)

avg = sum / len(list)
print(avg)

# Given a list of numbers, create a new list containing the square of each number.

numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]

result = []

for num in numbers:
    result.append(num * num)

print(result)

# Remove all duplicate values from a list while maintaining the order.

numbers = [4, 2, 7, 4, 2, 9, 7, 1, 5, 9, 3, 1]
numbers.sort()
uniqueNumbers = []

for num in numbers:
    if num not in uniqueNumbers:
        uniqueNumbers.append(num)

print(uniqueNumbers)

# Write a program that finds the largest and smallest number in a list without using max() or min() functions.

# maximum number
numbers = [12, 45, 7, 23, 89, 3, 67, 34, 22, 10]
maxNumber = numbers[0]

for num in numbers:
    if num > maxNumber:
        maxNumber = num

print(f"maximum number {maxNumber}")

# minimum number

minNumber = numbers[0]

for num in numbers:
    if num < minNumber:
        minNumber = num
    
print(f"minimum number is {minNumber}")

# Given a list of words, count how many vowels are present in all the words combined.
words = ["apple", "banana", "grape", "orange", "kiwi", "melon"]

vowels = ["a", "e", "i", "o", "u"]
vowelsCount = 0

for word in words:
    for char in word:
        if char in vowels:
            vowelsCount += 1

print(vowelsCount)