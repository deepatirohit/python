# default arguments = A default value for certain paramaters
#   default is used when that argument is omitted
#   make your functions more flexible, reduces of arguments
#  1. positional,   2. DEFAULT,     3. Keyword,     4. arbitary


def net_price(list_price, discount, tax):
    return list_price * (1- discount) * (1 + tax)


list_price = 500
discount = 0
tax = 0.05
print(net_price(list_price,discount, tax ))
 
def net_price(list_price,discount=0, tax=0.03):
    return list_price * (1- discount) * (1 + tax)


list_price = 500
print(net_price(list_price))


import time

# def count(start, end):
def count(end, start=0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("Done")
    
# count(10)
# count(20)

# keyword arguments
#  You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

# This way the function will receive a tuple of arguments, and can access the items accordingly:

def my_function(*kids):
    print(type(kids)) #<class 'tuple'>
    print(kids[0])
    print(kids[1])
    print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# **kwargs - allows you to pass multiple keyword-arguments

def student_info(**kwargs):
    print(type(kwargs)) #<class 'dict'>
    print("Student Information:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

student_info(name="John", age=23, course="Python", location="Seatle")

def add(*args):
    total = 0
    
    for arg in args:
        total += arg
    return total

print(add(1,2,3, 4, 5, 6, 7, 8, 9))