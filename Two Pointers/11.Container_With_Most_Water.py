"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.
"""

def maxArea(height):
    l, r = 0, len(height) - 1
    max_area = 0
    while l < r:
        if height[l] < height[r]:
            min_height = height[l]
        else:
            min_height = height[r]
        base = r - l
        area = base * min_height
        max_area = max(max_area, area)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return max_area

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))
