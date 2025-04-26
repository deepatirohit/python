# static methods = A method that belong to a class rather than any object from that class (instance)
# usaully used for generally utility function

# Instance methods  - best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not need acces to class data.

class Employee:
    
    def __init__(self, name, position):
        self.name = name
        self.position = position
        
        # instance method
    def get_info(self):
        return f"{self.name} = {self.position}"
    
    # static method
    @staticmethod
    def is_valid_position(position):
        valid_position = ["Manager", "Cashier","Cook", "Teacher"]
        return position in valid_position
    
# calling class method
employee1 = Employee("bob","Cook")

print(employee1.get_info())
print(employee1.is_valid_position("Teacher"))

# calling static method
print(Employee.is_valid_position("Cook"))
print(Employee.is_valid_position("Software engineer"))
print(Employee.is_valid_position("Lawyer"))