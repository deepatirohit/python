# Python, decorators are a powerful and flexible way to modify or extend the behavior of functions or methods.

# a function that takes another function as an argument and returns a new function with enhanced functionality.


def my_decorator(func):
    def wrapper():
        print("Something before the function runs.")
        func() 
        print("Something after the function runs.")
    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


say_hello()


def login_required(func):
    def wrapper(user):
        if user.get("is_logged_in"):
            return func(user)
        else:
            print(f"Access denied for {user['name']}. Please log in first!")
    return wrapper


@login_required
def view_profile(user):
    print(f"Welcome {user['name']}! This is your profile page.")

@login_required
def view_dashboard(user):
    print(f"Hello {user['name']}! This is your dashboard.")


user1 = {"name": "Alice", "is_logged_in": True}
user2 = {"name": "Bob", "is_logged_in": False}


view_profile(user1)  
view_dashboard(user2)  
