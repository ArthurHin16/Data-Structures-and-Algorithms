# Dictionaries are versatile data structures that stores key-value pairs.

# get(value, default) -> returns the value for a specified key.
my_dict = {'a': 1, 'b': 2}
value = my_dict.get('c', 0)
print(value)

# items() -> returns a new view of the dictionary´s items (key-value pairs)
items = my_dict.items()
print(items)

# keys() -> returns a new view of the dictionary´s keys
keys = my_dict.keys()

# values() -> returns a new vie of the dictionary´s values
values = my_dict.values()

# ITERATION
my_dict = {'a': 1, 'b': 2}
for key, value in my_dict.items():
    print(key, value)

# DICTIONARY COMPREHENSION
keys = ['a', 'b', 'c']
values = [1, 2, 3]
new_dict = {k: v for k, v in zip(keys, values)}