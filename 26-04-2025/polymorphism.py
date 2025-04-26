# polymorphism = Greek word that means to "have many forms or faces"
# poly = many  and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.
# Morphe = faces

# Two ways to achieve Polymorphism
# 1. Inheritance = An object could be treated of the same type as a parent class
# "Duck typing" = Object must have necessary attributes/methods.

class Shape:
    def area(self):
        print("Area of shape is undefined")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 7)
]


for shape in shapes:
    print(f"Area: {shape.area()}")
    
    
class Payment:
    def pay(self, amount):
        self.amount = amount,

class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paying ₹{amount} using Credit Card.")

class PayPal(Payment):
    def pay(self, amount):
        print(f"Paying ₹{amount} using PayPal.")

class UPI(Payment):
    def pay(self, amount):
        print(f"Paying ₹{amount} using UPI.")


def make_payment(payment_method, amount):
    payment_method.pay(amount)


credit = CreditCard()
paypal = PayPal()
upi = UPI()


make_payment(credit, 500)
make_payment(paypal, 300)
make_payment(upi, 200)
