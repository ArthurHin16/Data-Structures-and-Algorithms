# zip() -> Is used to combine multiple iterables element-wise into tuples. 

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = zip(list1, list2)

for item in zipped:
    print(item)


# Convert zip object to a list of tuples
zipped_list = list(zipped)
print(zipped_list) 

"""
When to use zip():

When you need to iterate over two data structures in parallel, such as lists or tuples, 
zip() can be used to combine them and iterate over the pairs simultaneously.
"""
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")