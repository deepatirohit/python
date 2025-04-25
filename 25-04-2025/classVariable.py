# Class variables = shared among all instances of a class
# Defined outside the constructor
#  Allow you to share data among all objects created from that class.

class Student:
    
    class_year = 2025
    num_students = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1
        
Student1 = Student("Zeal", 24)
Student2 = Student("Josh", 29)
Student3 = Student("Sam", 35)
Student4 = Student("sandy", 34)

print(Student1.name)
print(Student1.age)
print(Student1.class_year)

print(Student2.name)
print(Student2.age)
print(Student2.class_year)

print(Student.class_year)
print(Student.num_students)

print(f"My graduation class of {Student.class_year} has {Student.num_students} students.")

print(Student1.name)
print(Student2.name)
print(Student3.name)
print(Student4 .name)