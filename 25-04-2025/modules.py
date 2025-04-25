# module = a file containing code you want to include in your program
# use "import" to include a module (built-in or your own)
#  useful to breakup a large program reusable separate files

import math
import math as m
from math import pi

# print(help("math"))

print(math.pi)

print(m.pi)
print(pi)
print(m.e)

a, b, c, d = 1, 2, 3, 4

print(math.e **a)
print(math.e **b)
print(math.e **c)
print(math.e **d)

import helper

result = helper.pi

result = helper.square(2)
print(result)

result = helper.square(4)
print(result)

result = helper.square(10)
print(result)


result = helper.cube(4)
print(result)

result = helper.cube(12)
print(result)

result = helper.cube(33)
print(result)

result = helper.cube(14)
print(result)

result = helper.cube(10)
print(result)

result = helper.area(3)
print(result)

result = helper.circumference
print(result)
