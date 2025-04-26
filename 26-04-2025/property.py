# property = Decorator used to define a method as a property (it can be accessed like an atrribute)
# benefit: Add additional logic when read, write, or delete attributes
# Gives you getter, setter, add deleter methods

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
      
    @property  
    def width(self):
        return self._width  
    
    @property
    def height(self):
        return self._height  
    
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("with must be greater than zero")
            
        
    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than zero")
            
    @width.deleter
    def width(self):
        del self._width
        print("width has been deleted")
        
    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")
        
rectangle = Rectangle(3, 4)

rectangle._width = 5
rectangle._height = 6

del rectangle.width
del rectangle.height

# print(rectangle.width)  
# print(rectangle.height)

