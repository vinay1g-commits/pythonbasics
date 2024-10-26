#functions allows to encapsulate reusable code
#def keyword followed by the function name and parentheses.
# Any parameters are listed within the parentheses.

def add(a,b):
    return a+b

result = add(2,3)
print(result)

"""
Functions make the code modular and reusable. In automation testing, 
you might write functions for common actions like logging in, 
navigating through pages, etc.
"""

def greet(name):
    print(f"hello {name}")

greet("vinay") #calling a function

#Default parameter
def greet2(name = "raju"):
    print(f"hi {name}")
greet2()

"""
Variable-Length Arguments
You can allow a function to accept a variable number of arguments using 
*args and **kwargs
"""

def number(*args):
    print(args)
number(1,2,3,4)

def keyval(**kwargs):
    print(kwargs)
keyval(neme="vinay",city = "mumbai")


"""
Variables defined inside a function are in the local scope and can 
only be accessed within that function.

Variables defined outside any function are in the global scope
and can be accessed from anywhere in the code.

In nested functions, the outer function's variables are in the enclosing scope.

Python has a built-in scope that contains names such as print() and len(), 
which are always available.

"""

def outer_function():
    z = 20  # Enclosing variable

    def inner_function():
        print(z)  # Accesses the enclosing variable

    inner_function()

outer_function()  # Output: 20
