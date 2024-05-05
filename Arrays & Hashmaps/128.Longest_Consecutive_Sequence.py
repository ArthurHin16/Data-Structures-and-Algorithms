"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
"""
def longestConsecutive(nums):
        numbers = set(nums)
        longest_sequence = 0
        for num in nums:
            if (num - 1) not in numbers:
                length = 0
                while (num + length) in numbers:
                    length += 1
                longest_sequence = max(longest_sequence, length)
        return longest_sequence

nums = [100,4,200,1,3,2]
print(longestConsecutive(nums))