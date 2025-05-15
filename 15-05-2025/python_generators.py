# A generator function is a special type of function that returns an iterator object.

import sys

def mygenerator():
    yield 1
    yield 3
    yield 2
    yield 4

g = mygenerator()

# for i in g:
#     print(i)
    
# value = next(g)
# print(value)

# value = next(g)
# print(value)

print(sum(g))
 
def countdown(num):
    print("starting")
    while num > 0:
        yield num
        num -= 1
        
cd = countdown(4)

value = next(cd)
print(value)

print(next(cd))
print(next(cd))
print(next(cd))


def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1

print(sum(firstn_generator(10)))
print(sys.getsizeof(firstn_generator(10)))

def fibonacci(limit):
    # 0 1 2 3 5 ...
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a+b

fib = fibonacci(20)

result = []
for i in fib:
    result.append(i)
    # print(i)
    
print(result)

# generator expression
mygenerator = (i for i in range(10) if i%2 == 0)

for i in mygenerator:
    print(i)
    
# listcomprehension
mylist = [i for i in range(10) if i%2 == 0]

for i in mylist:
    print(i)
    
print(sys.getsizeof(mygenerator))
print(sys.getsizeof(mylist))