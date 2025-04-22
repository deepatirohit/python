import math

print(math.pi)

# square root
x = 9

squareRootOfX = math.sqrt(x)
print(squareRootOfX)

y = 9.2

ceilNumberOfy = math.ceil(y)
print(ceilNumberOfy)


num = 9.9
floorNumber = math.floor(num)
print(floorNumber)

# circumferance of circle
# radius = float(input("What is the radius of circle?: "))
# circumferance = 2 * math.pi * radius

# print(f"The circumference of circle is {circumferance}")

# print(f"The circumference of circle is {round(circumferance)}")

# area of circle (area = πr2)

# radius = float(input("Enter the radius: "))

# area = math.pi * pow(radius, 2)

# print(f"area of circle is {area}")
# print(f"area of circle is {round(area, 2)}")

# Hypotenuse of triangle
a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"The hypotenus of triangle is {c}")