# PYTHON DECORATORS
# Decorator is a wrapper over a function that adds functionality to a function without changing the function codes
# Example

def my_decorator(function):  # decorator function : can have any function
    def wrapper(*args, **kwargs):  # wrapper to a function
        print("Good morning Kenya")  # Added features to the new function
        function(*args, **kwargs)  # Original function to be modified
        print("I give you my peace")  # Added features to the new function

    return wrapper  # We must return the wrapper ...wrapper function on return here has no brackets


@my_decorator  # put @decorator_function immediately before the function you want to modify
def my_name(name, age):  # Original function
    # ....
    print(f"Am {name} and am {age}yrs old")


my_name("Sam", age=30)  # Call your original function here 1

# my_name = my_decorator(my_name)   Second way then call it ...
# my_name()      # ...call it here

# The END, it was nice learning python decorators
