# class methods = Allow opertaions related to the class itself
# Take (cls) as the first parameter, which represents the class itself

# Instance methods = Best for operations on instances of the class
# static methods = Best for utility functions that do not need access to class data
# class methods = best for class-level data or require access to the class itself


class Student:
    
    count = 0
    
    def __init__(self, name, gpa):
        self.name = name
        self.gap = gpa
        Student.count += 1
      
    #   instance method  
    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    @classmethod
    def get_student_count(cls):
        return f"Total no of students: {cls.count}"

print(Student.get_student_count())
Student1 = Student("John", 3.7)
Student2 = Student("Zeal", 4.2)  
Student2 = Student("sandy", 3.2)  

print(Student.get_student_count())