# logical-operators = evaluate multiple conditions (or, and, not)
# or - atleast one condition must be true
# and - both conditions must be true
# not - inverts the condition (not False, not True);

# Operator      | Description               | Example
# and           | True if both are True     | a > 10 and b < 20
# or            | True if either is True    | a < 5 or b == 0
# not           | Reverses the condition    | not (a == b)

# or
temp = 25
temp = -2
temp = 40
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancel.")
else :
    print("The outdoor event is still scheduled")
    
# and

temp = 20
is_sunny = True

if temp >= 30 and is_sunny:
    print("It is Hot Outside")
elif temp <= 0  and is_sunny:
    print("It is cold outside")
elif temp < 30 and temp > 0 and is_sunny: #(30 > temp > 0)
    print("It is warm outside")

# ex:1 Check if a number is between 50 and 100

num = int(input("Enter a number between 50 - 100: "))
is_Between = False

if (num >= 50) and (num <= 100):
    is_Between = True
    print(is_Between)
else:
    print("This is invalid, the num should be between 50 - 100")

# Check if a person can vote

age = int(input("What is your age?: "))
is_eligible = True

if age >= 18 and is_eligible:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote, you should have atleast 18 years to vote.")

# Check if a username is valid

username = input("Enter your name: ")
is_valid = False

if username != "":
    is_valid = True
    print(f"{username} is valid")
else:
    print("username can not be empty")

#  Check if a student passed
maths_marks = int(input("Enter your maths marks: "))
science_marks = int(input("Enter your science marks: "))

if (maths_marks < 0 or maths_marks > 100) or (science_marks < 0 and science_marks > 100): 
    print("marks should be between 0 and 100")
elif (maths_marks >= 35) and (science_marks >= 35):
    print("You have passed.")
else:
    print("sorry, you have failed")

#  Validate login

username = input("Enter your user name: ")
password = input("Enter your password: ")

if username == "":
    print("user name is required")
elif len(password) == 0:
    print("Password required")
elif len(password) < 8 :
    print("password should be atleast 8 characters")
else:
    print("Your logged in")

# conditional expressions = A one line shortcut for the if-else statement (ternary operator)
                            # print or assign one of two values based on a condition
                            # x if condition else y
                            

# num = int(input("Enter a number: "))

# print("Positive" if num > 0 else "Negative")

# result = "Even" if num %2 == 0 else "Odd"
# print(result)

a = 4
b = 7
max_num = a if a > b else b
min_num = a if a < b else b

print(f"maximum number is {max_num}")
print(f"minimum number is {min_num}")