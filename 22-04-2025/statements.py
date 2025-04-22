#  Check if a number is positive, negative, or zero
num = int(input("Enter a number: "))

if num > 0:
    print(f"{num} is positive number.")
elif num < 0:
    print(f"{num} is negative number.")
else:
    print(f"{num} is zero")



#  Check if a number is divisible by both 3 and 5

num = int(input("Enter a number: "))

if num % 3 == 0 & num % 5 == 0:
    print(f"{num} is divisible by both 3 and 5")
else :
    print(f"{num} is not divisible by both 3 and 5")

# Check if a year is a leap year

year = int(input("Enter a year: "))

if (year % 4 ==0):
    if (year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is leap year.")
else:
        print(f"{year} is not a leap year")

#  marks Grading System

marks = int(input("Enter your marks: "))

if(marks >= 90):
    print("You got A+")
elif (marks >= 80):
    print("You got A grade.")
elif (marks >= 70):
    print("you got B grade")
elif (marks > 40):
    print("you got C grade")
else:
    print("You are failed.")

#  check whether a character is a vowel or consonant.

char = input("Enter a char: ")

if len(char) > 1:
    print("Enter single character only")
elif char.lower() in ["a", "e", "i", "o", "u"]:
    print(f"{char} is a vowel")
else:
    print(f"{char} is a consonant")

# Check if a number is even or odd 
num = int(input("Enter a number: "))

if (num % 2 == 0):
    print(f"{num} is even number")
else:
    print(f"{num} is odd number")
    
# Age Group Checker

age = int(input("Enter age: "))

if (age >= 20):
    print("You are an adult")
elif (age >= 13):
    print("You are teen")
elif (age > 0):
    print("You are child")
else:
    print("you are not yet born")

# Traffic Light Color

color = input("Choose one color [red, green, yellow]: ")

color = color.lower()  

if color == "red":
    print("Stop")
elif color == "green":
    print("Go")
elif color == "yellow":
    print("Slow down")
else:
    print("Invalid input! Please choose from red, green, or yellow.")
