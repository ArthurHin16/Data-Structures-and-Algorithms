"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
ans[i] is the number of 1's in the binary representation of i.
"""

# Solution with Dynamic Programming
# Time Complexity O(n)
# Space Complexity O(n)

from collections import Counter

def countBits(n):
    dp = [0] * (n + 1)
    offset = 1
    for i in range(1, n + 1):
        if offset * 2 == i:
            offset = i
        dp[i] = 1 + dp[i-offset]
    return dp

# Time Complexity O(n log n)
# Space Complexity O(n)
def countBits(n):
    result = []
    for i in range(n + 1):
        binary_number = bin(i)[2:] # This operations costs O(log n)
        binary_number = Counter(binary_number)
        result.append(binary_number['1'])
    return result
