"""
sets are unique unordered mutable collection of items. it is used to avoid duplicates
it supports operations like union intersection and difference
"""

my_set = {1,2,3,4,4}
print(my_set)

set1 = {1,2,3,4}
set1.add(5)
print(set1)

set1.remove(1) # raises an error
print(set1)

set1.discard(2) # it doesnt raise an error
print(set1)

set2 = {1,2,3,4}
set3 = {3,4,5,6}

union  = set2 | set3 # Combines elements from two sets.
print(union)

intersection = set2 & set3 # Gets common elements.
print(intersection)

difference = set2 - set3 #Elements in one set but not in the other.
print(difference)

difference2 = set3 - set2 #Elements in one set but not in the other.
print(difference2)

symmetric_diff = set2 ^set3 # Elements in either set but not in both.
print(symmetric_diff)

#You can check if an element is in a set using the in keyword.
print(2 in set1)
print(2 in set2)

#Iterating Through a Set: You can loop through a set using a for loop.
for iter in set1:
    print(iter)

# sets are often used for tasks like removing duplicates from a list:
set5 = [1,2,3,3,5,5,6,]
print(set5)
list = set(set5)
print(list)
