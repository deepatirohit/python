# super() = Function used in a child class to call methods from parent class (super class).
# Allows you to extend the functionality of the inherited methods.

class Parent:
    def __init__(self, name):
        self.name = name
        
    def printName(self):
        print(f"Hi, I'm {self.name}")

class Child(Parent):
    def __init__(self, name):
        super().__init__(name)
 
#  The super() function is used to give access to methods and properties of a parent or sibling class.

# The super() function returns an object that represents the parent class.      

person1 = Child("John")
person2 = Child("Mary")
person3 = Child("Sophia")
person4 = Child("Zeal")
person5 = Child("Angelina")

person1.printName()
person2.printName()
person3.printName()
person4.printName()
person5.printName()

class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal created: {self.name}")
    
    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        print(f"Dog breed: {self.breed}")
    
    def speak(self):
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        print(f"Cat breed: {self.breed}")
    
    def speak(self):
        print(f"{self.name} says Meow!")

class Rabbit(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        print(f"Rabbit breed: {self.breed}")
    
    def speak(self):
        print(f"{self.name} thumps silently!")

# Creating instances
dog = Dog("Buddy", "Labrador")
cat = Cat("Whiskers", "Siamese")
rabbit = Rabbit("Fluffy", "Angora")

# Calling speak method for each
dog.speak()
cat.speak()
rabbit.speak()
