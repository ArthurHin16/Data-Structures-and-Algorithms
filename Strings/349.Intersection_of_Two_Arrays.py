"""
Given two integer arrays nums1 and nums2, return an array of their 
intersection.
Each element in the result must be unique and you may return the result in any order.
"""

def intersection(nums1, nums2):
        set_nums1 = set()
        set_nums2 = set()
        for num in nums1:
            set_nums1.add(num)
        for num in nums2:
            set_nums2.add(num)
        return list(set_nums1 & set_nums2)

nums1 = [1,2,2,1]
nums2 = [2,2]
print(intersection(nums1, nums2))