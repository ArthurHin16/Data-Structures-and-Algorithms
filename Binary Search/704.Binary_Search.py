"""
Given an array of integers nums which is sorted in ascending order, and an integer target, 
write a function to search target in nums. If target exists, then return its index. 
Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""


def search(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        midd = (l + r) // 2
        if nums[midd] == target:
            return midd
        elif nums[midd] > target:
            r -= 1
        else:
            l += 1
    return -1


nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(search(nums, target))
