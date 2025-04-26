# exception = An event interrupts the flow of a program.
#       (zeroDivisionError, TypeError, ValueError)
#       1.try   2.except    3.finally


try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Please enter a valid number!")
else:
    print("Division successful!")
finally:
    print("Thank you for using the program.")
