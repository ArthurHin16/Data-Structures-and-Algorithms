"""
Write a function that takes the binary representation of a positive integer and returns the number of 
set bits it has (also known as the Hamming weight).
"""

# Time Complexity: O(log n)
# Space Complexity: O(log n)

def hammingWeight(n):
    return str(bin(n)[2:]).count('1')

n = 11
print(hammingWeight(n))