"""
You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value 
and return this value. Any answer with a calculation error less than 10-5 will be accepted.
"""


def findMaxAverage(nums, k):
    total_sum = sum(nums[:k])
    window = total_sum
    for i in range(1, len(nums) - k + 1):
        window = window - nums[i-1] + nums[i + k - 1]
        total_sum = max(window, total_sum)
    return total_sum / k

nums = [1,12,-5,-6,50,3]
k = 4
print(findMaxAverage(nums,k))
