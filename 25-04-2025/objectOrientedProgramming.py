# Object - A "bundle" of related attributes (varaibles)  and methods (functions)
# object is an instance of a class
# ex.phone, cup, book
# you need a "class" to create many objects.

# class - (blueprint) used to design the structure and layout of an object
# dunder = double underscore __

class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
        
car1 = Car("Mustang", 2020, "White", False)
print(car1)
print(car1.color)
print(car1.model)
print(car1.year)
print(car1.for_sale)

car2 = Car("KIA", 2024, "Red", True)

print(car2.color)
print(car2.model)
print(car2.year)

class Student:
    def __init__(self, name, year, rollNumber):
        self.name = name
        self.year = year
        self.rollNumber = rollNumber
    
student1 = Student("John", 1, "00123")
student2 = Student("Peter", 3, "00125")

print(student1.name)
print(student1.year)
print(student1.rollNumber)

from personHelper import Person

person1 = Person("Marry", 23, "USA", "23434")
person2 = Person("James", 25, "Canada", "1234")
person3= Person("Kate", 24, "Seatle", "23434")

print(person1.name)
print(person1.age)
print(person1.place)

print(person2.name)
print(person2.age)
print(person2.phone)

print(person3.name)
print(person3.phone)
print(person3.place)

print(person1.eat("biryani"))
print(person1.sleep())

print(person2.introduce())
print(person2.drive())

print(person3.eat("Pizza"))