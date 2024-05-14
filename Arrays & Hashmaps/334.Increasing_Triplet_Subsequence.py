"""
Given an integer array nums, return true if there exists a triple of indices (i, j, k)
such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
"""

def increasingTriplet(nums):
    first = float('inf')
    second = float('inf')
    for num in nums:
        if num <= first:
            first = num
        elif num <= second:
            second = num
        else:
            return True
    return False

nums = [1,2,3,4,5]
print(increasingTriplet(nums))
