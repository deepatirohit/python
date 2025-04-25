# methods are actions that perform on objects
class Person:
    def __init__(self, name, age, place, phone):
        self.name = name
        self.age = age
        self.place = place
        self.phone = phone
        
    def drive(self):
        print(f"{self.name} is driving.")
    
    def sleep(self):
        print(f"{self.name} is sleeping.")

    def walk(self):
        print(f"{self.name} is walking in {self.place}.")

    def eat(self, food):
        print(f"{self.name} is eating {food}.")

    def call(self, contact_name):
        print(f"{self.name} is calling {contact_name} using {self.phone}.")
        
    def introduce(self):
        print(f"Hi, I'm {self.name}, I'm {self.age} years old and I live in {self.place}.")
