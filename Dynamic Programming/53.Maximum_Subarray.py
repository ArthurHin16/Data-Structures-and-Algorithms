# Given an integer array nums, find the subarraywith the largest sum, and return its sum.

def maxSubArray(nums):
    max_current = nums[0]
    max_global = nums[0]
    for i in range(1, len(nums)):
        max_current = max(max_current + nums[i], nums[i])
        if max_current > max_global:
            max_global = max_current
    return max_global


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(nums))
