# errors and exceptions

# sytax error
# Occurs when Python code is not written correctly

def say_hello()
    print("Hello")

print(("This is syntax error example")

# type error
# Happens when an operation or function is applied to an object of inappropriate type.

add = 5 + '10'
print(add)

# ModuleNotFoundError
# Raised when trying to import a module that doesn't exist.

import non_existent_module

# NameError
# Occurs when a variable or function name is not defined.
a = 5
b = a + c
print(b)

# FileNotFoundError
# Raised when trying to open a file that doesn't exist.
with open("nonexistent_file.txt", "r") as file:
    data = file.read()

# valueError
number = int('abc')
print(number)

# IndexError
# Raised when trying to access an index that’s out of range in a sequence.

my_list = [1, 2, 3]
print(my_list[5])

# KeyError
# Occurs when trying to access a dictionary with a key that doesn’t exist.
my_dict = {"name": "Alice"}
print(my_dict["age"])

# raise Exception
x = -5
if x < 0:
    raise Exception("x should be positive")

#Assertion Error
x = -5
assert (x >= 0), 'X is not positive'

# zerodivisionError
try:
    a = 5/0
except:
    print("an error happend")

try:
    a = 5/0
except Exception as e:
    print(e)

try:
    a = 5/0
    b = a + "10"
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)

    
try:
    a = 10/5
    b = a + 10
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print("Everything is fine")
finally:
    print("cleaning up...")