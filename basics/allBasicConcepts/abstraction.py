"""
Abstraction is about hiding complex implementation details and exposing
only the necessary parts of an object. It simplifies interaction with
complex systems by providing a clear interface.
"""

class Animal:
    def speak(self):
        pass

class cat(Animal):
    def speak(self):
        print('meow')

class dog(Animal):
    def speak(self):
        print("bow")

def display_info(pos):
    pos.speak()

c= cat()
d= dog()
display_info(c)
display_info(d)