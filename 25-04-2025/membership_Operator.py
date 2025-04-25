# membership operator = used to test whether a value or variable is found in sequence
# 1. in
# 2. not in

word = "APPLE"

letter = input("Guess a letter in the secret word: ").upper()

if letter in word:
    print(f"There is a {letter}")
else:
    print(f"{letter} was not found")
    
if letter not in word:
    print(f"{letter} was not found")
else:
    print(f"There is a  {letter}")
    
    
students = {"bob", "peter", "sandy", "mary"}

student = input("Enter the name of a student: ")

if student in students:
    print(f"{student} is a student")
else:
    print(f"{student} was not found")
    
if student not in students:
    print(f"{student} was not found")
else:
    print(f"{student} is a student")
    
grades = {
    "John": "a",
    "Anjali": "b",
    "Karan": "c",
    "Sneha": "d",
    "Vikram": "e"
}


student = input("enter a student name: ")

if student in grades:
    print(f"{student}'s igrade is {grades[student]} student")
else:
    print(f"{student} was not found")
    
email = "test@gmail.com"

if "@" in email and "." in email:
    print("valid email")
else:
    print("Invalid email.")