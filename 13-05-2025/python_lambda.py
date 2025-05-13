# A lambda function is a small, anonymous function in Python
# lambda arguments: expression

add10 = lambda x: x + 10
print(add10(5))

multiplication = lambda x,y: x * y
print(multiplication(10, 5))

square = lambda x: x * x
print(square(5)) 

add = lambda a, b: a + b
print(add(3, 4)) 

nums = [1, 2, 3, 4]
squares = list(map(lambda x: x * x, nums))
print(squares)

nums = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)