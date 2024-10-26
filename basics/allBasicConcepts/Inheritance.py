"""
Inheritance allows a class (called a child or derived class) to inherit
attributes and methods from another class (called a parent or base class).
This promotes code reuse and establishes a hierarchical relationship between classes.
"""

class parent:
    def name(self):
        print("p_name")
    def age(self):
        print("p_age")

class child(parent):
    def profession(self):
        print("IT")

    def name(self):
        print("child_name")

class child2(parent):
    def profession(self):
        print("Doctor")

    def name(self):
        print("child_name2")

obj = child2()
print(obj.name(),obj.age(),obj.profession())





