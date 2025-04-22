# 1.strings (strings in python are surrounded by either single quotation mark or double quotation marks)
greetings = "Good morning"
message = "Hello"+ ', ' + greetings

# # len to count the number of chars in a stringD
print(len(message)) 
print(message)

# slicing string

varString = "practicing the pythong string methods"

print(varString[:10])
print(varString[0:3])
print(varString[:-1])
upperCaseString = varString.upper()
lowerCaseString = varString.lower()

print(upperCaseString)
print(lowerCaseString)

# split() method split a string into a list
splitString = varString.split()
print(splitString)

text = "Practicing the string slicing method"
replacingText = text.replace("slicing",  "manipulation")

print(replacingText)

messy = "   Clean   this   string    "

removingSpaces = messy.replace(" ", "")
print(removingSpaces)

fruits = "apple, banana, apple, orange, apple"
appleCount = fruits.count("apple")
bananaCount = fruits.count("banana")
orangeCount = fruits.count("orange")
grapesCount = fruits.count("grapes")
print(appleCount)
print(bananaCount)
print(orangeCount)
print(grapesCount)

senetence = "Python is fun"
reverseSentence = senetence[::-1]
print(reverseSentence)

captilizeSentence = senetence.capitalize()
print(captilizeSentence)

titleCase = senetence.title()
print(titleCase)

name = "John"
language = "Python"

print(f"Hi, I'm {name}, I love {language}")

email = "john.peter@gmail.com"
extractName = email.split("@")[0]
extractDomain = email.split("@")[1]
print(extractName)
print(extractDomain)

# modifying string
varString ="practicing the modifying string method"
varString = "string modified"
print(varString)
