# Multiple inheritance = inherit from more than one parent class
                        # C(A, B)
# multilevel inheritance = Inherit from a parent which inherits from another parent.
#           C(B) < - B(A) <- A

class Animal:
    def __init__(self, name):
        self.name = name
        
    def eat(self):
        print(f"{self.name} is eating")
        
    def sleep(self):
        print(f"{self.name} is sleeping.")
    

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey):
    pass
    
class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

# rabbit = Rabbit()
# hawk = Hawk()
# fish = Fish()



# fish.sleep()

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

rabbit.flee()
fish.flee()
fish.hunt()

rabbit.eat()
fish.eat()


hawk.eat()
hawk.sleep()