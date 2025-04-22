# type casting = the process of converting a variable from one data type to another data type str(), float(), int(), bool()

# name = "john"
# age = 25
# is_student = True

# print(type(name))
# print(type(age))
# print(type(is_student))

# name = bool(name)
# print(name)

# age = str(age)
# print(age)
# print(type(age))

# name = ""
# name = bool(name)
# print(name)

# input() =  A function that prompts the user to enter data returns the entered data as a string
# userInput =  input("Enter your name: ")
# userAge = input("Enter your age: ")
# # userAge = int(input("Enter your age: "))
# userAge = int(userAge) + 1
# print(f"Hello, I'm {userInput} and,  I'm {userAge} years old")

# Exercise 1

# length = int(input("Enter the length: "))
# width = int(input("Enter the width: "))

# area = length * width
# print(area)

# Exercise 2 shopping cart
item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))

totalPrice = price * quantity
print(f"You have bought {quantity} x {item}s")
print(f"Your total is {totalPrice}")