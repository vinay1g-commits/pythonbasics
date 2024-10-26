"""
Polymorphism allows objects of different classes to be treated as
objects of a common base class. It enables the same method to behave
differently based on the object that calls it.
"""
from basics.allBasicConcepts.Inheritance import child2


class Parent:
    def name(self):
        print("p_name")

    def age(self):
        print("p_age")


class Child(Parent):
    def profession(self):
        print("IT")

    def name(self):
        print("child_name")


class Child2(Parent):
    def profession(self):
        print("Doctor")

    def name(self):
        print("child_name2")


c1 = Child()
c2 = Child2()

#function to display polymorphism

def display_info(obj):
    obj.name()
    obj.age()
    obj.profession()

# Display information for both objects
display_info(c1)
display_info(c2)