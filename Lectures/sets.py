# set() Sets are unordered collections of unique elements.

my_set = {1, 2, 3}

my_set.add(4) # Adds an element that is not already present.
new_set = my_set.copy() # returns a shallow copy of the set.
my_set.discard(2) # removes an element from the set if it´s a member.
my_set.remove(2) # removes an element from the set if it´s a member, if not raises a KeyError.
my_set.clear() # removes all elements from the set.

# ADVANCED METHODS AND FUNCTIONALITIES

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# union() -> Returns a new set containing all disctinct elements from both sets.
union_set = set1.union(set2)
union_set = set1 | set2
print(union_set) 

# intersection() -> Returns a new set containing common elements from both sets.
intersection_set = set1.intersection(set2)
intersection_set = set1 & set2
print(intersection_set)

# difference() -> Returns a new set containing elements that are present in the first set 
# but not in the second set.
difference_set = set1.difference(set2)
difference_set = set1 - set2
print(difference_set)