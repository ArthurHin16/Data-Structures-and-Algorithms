"""
Given an integer array nums and an integer k, return true if there are two distinct indices
i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
"""


def containsNearbyDuplicate(nums):
    hashmap = {}
    for i in range(len(nums)):
        if nums[i] in hashmap and (abs(i - hashmap[nums[i]]) <= k):
            return True
        else:
            hashmap[nums[i]] = i
    return False

nums = [1,2,3,1]
k = 3
print(containsNearbyDuplicate(nums))