# Iterables = An object/collection that can return its elements one at a time, allowing it to be iterated over in a loop.

numbers = [1, 2, 3, 4, 5, 6]

for number in numbers:
    print(number)
    
for number in reversed(numbers):
    # print(number)
    print(number, end="-")
    
numbers = (1, 2, 3, 4, 5, 6)

for item in numbers:
    # print(item,end=",")
    print(item)
    

fruits = {"apple", "orange", "banana", "kiwi"}

for fruit in fruits:
    print(fruit)
    
text = "python is a programming language"

for char in text:
    print(char)
    
student = {
    "name": "John",
    "age": 22,
    "course": "Python Programming",
    "isEnrolled": True
}


for key in student:
    print(key)
    
for value in student.values():
    print(value)
    
for item in student.items():
    print(item)
    
for key, value in student.items():
    print([key, value])