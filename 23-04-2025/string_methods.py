# capitalize()	Converts the first character to upper case

name = "hello, and welcome to python string methods"

print(name.capitalize()) #Hello, and welcome to python string methods

# casefold() and lower()	Converts string into lower case

text = "HELLO, AND WELCOME TO PYTHON STRING METHODS"

caseFoldText = text.casefold()
lowercaseText = text.lower()
print(lowercaseText)
print(caseFoldText)
# hello, and welcome to python string methods

# count()	Returns the number of times a specified value occurs in a string

word = "hello, and welcome to python string methods"

print(word.count("e"))
print(word.count("h"))

# len() -  return the length of the string

text = "hello, and welcome to python string methods"

print(len(text))

# find() -  returns the index of first occurance of a give character

text = "hello, and welcome to python string methods"

print(text.find("o"))

# rfind() - retuns the index of last occurance of a give character

text = "hello, and welcome to python string methods"
print(text.rfind("o"))
print(text.rfind("n"))
print(text.rfind("z")) #if not return -1

# upper() -  converts the string into upper case letter
text = "hello, and welcome to python string methods"
print(text.upper())

# is digit() -   method is used to check whether all characters in a string are digits returns bool (true or false)

word = "123456"
text = "hello, and welcome to python string methods"
print(word.isdigit())
print(text.isdigit())

# isalpha() -  method is used to checl whether all the characters in a string are only alpabetical characters
word = "123456"
text = "string"

print(word.isalpha())
print(text.isalpha())

print(help(str)) 


# exercise - validate username
# 1 username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

userName = input("Enter your name: ")

if len(userName) >= 12:
    print("User name should be less than 12 characters")
elif not userName.find(" ") == -1:
    print("username must not contain spaces")
elif not userName.isalpha():
    print("User name must not contain digits")
else:
    print("user name is valid") 

