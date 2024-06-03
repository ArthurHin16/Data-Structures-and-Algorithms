"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
"""

# Time Complexity O(n^3)
def threeSum(nums):
    three_sum_set = set()
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                three_sum = nums[i] + nums[j] + nums[k]
                if three_sum == 0:
                    values = [nums[i], nums[j], nums[k]]
                    values.sort()
                    three_sum_set.add(tuple(values))
    ans = [list(tpl) for tpl in three_sum_set]
    return ans

def three_sum_extra_memory(nums):
    nums.sort()
    values = set()
    for n in range(len(nums)):
        l = n + 1
        r = len(nums) - 1
        while l < r:
            total_sum = nums[n] + nums[l] + nums[r]
            if total_sum == 0:
                values.add(tuple([nums[n], nums[l], nums[r]]))   
                l += 1
                r -= 1
            elif total_sum > 0:
                r -= 1
            else:
                l += 1
    answer = [list(val) for val in values]
    return answer 

def three_sum_optimal_approach(nums):

    nums.sort()
    values = []

    for n in range(len(nums)):

        if n != 0 and nums[n] == nums[n-1]:
            continue

        l = n + 1
        r = len(nums) - 1
        while l < r:
            total_sum = nums[n] + nums[l] + nums[r]
            if total_sum == 0:
                values.append([nums[n], nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
                while l < r and nums[r] == nums[r+1]:
                    r -= 1
            elif total_sum > 0:
                r -= 1
            else:
                l += 1
    return values

