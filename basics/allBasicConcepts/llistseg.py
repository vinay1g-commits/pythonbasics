#lists are ordered and mutable collection of items.
#They can hold different data types

test_cases = ["login","signup","notification",10]
print(len(test_cases))
print(test_cases[0])
test_cases.append("extra")
print(test_cases)
test_cases.remove("extra")
print(test_cases)

"""
Lists in Python are mutable, meaning you can modify them after creation (add/remove elements). 
You can use indexing to access individual elements.
"""