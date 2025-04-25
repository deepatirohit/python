# inheritance = allows a class to inherit attributes and methods from another class
# Helps with code reusablity and extensibility
# class Child(parent)

class Animal:
    def __init__(self, name):
        self.name = name
        self.isAlive = True 
        
    
    def eat(self):
        print(f"{self.name} is eating")
        
    def sleep(self):
        print(f"{self.name}")
        
class Dog(Animal):
    def speak(self):
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("meow")

class Mouse(Animal):
    def speak(self):
        print("squeek")

dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Micky")

print(dog.name)
dog.eat()
dog.sleep()
dog.speak()
print(dog.isAlive)

print(cat.name)
cat.eat()
cat.sleep()
cat.speak()
print(cat.isAlive)

print(mouse.name)
mouse.eat()
mouse.sleep()
mouse.speak()
print(mouse.isAlive)