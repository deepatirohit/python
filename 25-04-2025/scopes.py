# varible scope = where a variable is visible and accessable
# A variable is only available from inside the region it is created. This is called scope.

# Local Scope
# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

def myfunc():
  x = 300
  print(x)

# print(x) #NameError: name 'x' is not defined
myfunc()

# The local variable can be accessed from a function within the function

def myfunc1():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc1()

# Global Scope
# A variable created in the main body of the Python code is a global variable and belongs to the global scope.

x = 300

def myGlobalFun():
  print(x)

myGlobalFun()

print(x)

# The function will print the local x, and then the code will print the global x:

x = 300

def myExamplefunc():
  x = 200
  print(x)

myExamplefunc()

print(x)

# Global Keyword
# If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.

# The global keyword makes the variable global.

def cart():
  global price
  price = 300

cart()

print(price)


# scope resolution = (LEGB) local -> enclosed -> global -> built-in
import math

def moduleFunc():
    print(math.pi)
    
print(math.pi)
moduleFunc()