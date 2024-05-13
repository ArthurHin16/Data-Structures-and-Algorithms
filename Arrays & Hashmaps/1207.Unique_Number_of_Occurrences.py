"""
Given an array of integers arr, return true if the number of occurrences
of each value in the array is unique or false otherwise.
"""

# Solution 1


def uniqueOccurrences1(arr):
    hashmap = {}
    for num in arr:
        hashmap[num] = hashmap.get(num, 0) + 1
    return len(hashmap) == len(set(hashmap.values()))


# Solution 2
def uniqueOccurrences2(arr):
    hashmap = {}
    unique_occurences = set()
    for num in arr:
        hashmap[num] = hashmap.get(num, 0) + 1
        for key, value in hashmap.items():
            if value in unique_occurences:
                return False
            unique_occurences.add(value)
        return True

