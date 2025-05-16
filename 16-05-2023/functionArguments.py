def print_name(name):#parameter
    print(name)
    
print_name("john")#arguments
print_name("Jimmy")
print_name("Rose")
print_name("Sarah")

def foo(a, b, c):
    print(a, b, c)
    
# positional arguments
foo(1, 2, 3)

# keyword arguments
foo(a=1, c=2, b=3)

# mixed arguments
foo(1, c=3, b=5)

# default arguments
def print_persons(a, b, c, d="james"):
    print(a, b, c, d)
    
print_persons("Peter", "haze", "Phil")
print_persons("Peter", "haze", "Phil", "Sarah")

# *args and **kwargs
def fooFunc(a, b, *args, **kwargs):
    print(a,b)
    
    for arg in args:
        print(arg)
        
    for key in kwargs:
        print(key, kwargs[key])
        
fooFunc(1,2, 3, 4, 5, 6, 7, 8, nine=9, ten=10)

# unppacking arguments
def unpackingFunc(a, b, c):
    print(a, b, c)
    
mylist = [1,2,3]
unpackingFunc(*mylist)

myTuple=(4, 5, 6)
unpackingFunc(*myTuple)

myDict = {'a':7, 'b':8, 'c':9}
unpackingFunc(**myDict)

# local vs global variables
# global variable
def foo():
    print(number)
    x = number
    print("Number inside the function", x)

number = 12
foo()

# local variable
def foo():
    global number
    number = 20
    print("number inside the function", number)
    
number = 30
foo()
print('number outside the function', number)
