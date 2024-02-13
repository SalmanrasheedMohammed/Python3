# SET
# Creating an empty set
empty_set = set()

# Creating a set with elements
my_set = {1, 2, 3, 4, 5}
print(my_set) # {1, 2, 3, 4, 5}


# Adding elements
my_set.add(7)
my_set.add(3)
print(my_set) # {1, 2, 3, 4, 5, 7}
# 3 was not added because it was already at set


# Removing elements
my_set.remove(3)
print(my_set) # {1, 2, 4, 5, 7}


# Set Operators
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union: Elements present in either set1 or set2 (or both)
union_set = set1.union(set2)  # Output: {1, 2, 3, 4, 5, 6}

# Intersection: Elements present in both set1 and set2
intersection_set = set1.intersection(set2)  # Output: {3, 4}

# Difference: Elements present in set1 but not in set2
difference_set = set1.difference(set2)  # Output: {1, 2}

# Symmetric Difference: Elements present in either set1 or set2, but not in both
symmetric_difference_set = set1.symmetric_difference(set2)  # Output: {1, 2, 5, 6}


# Iterating over a set
for element in my_set:
    print(element)
# output
"""
2
4
5
7
"""


# Duplicates elements from the set

my_list = [1, 2, 3, 4, 2, 3, 5]
a = set(my_list)
print(a)  # Output: {1, 2, 3, 4, 5}




