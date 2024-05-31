def sortColors(nums):
    counts = [0, 0, 0]
    for n in nums:
        counts[n] += 1
    # [3, 2, 1] 3: 0, 2: 1, 1: 2 [0,0,0,1,1,2]
    start = 0
    for i in range(len(counts)):  # 3
        for j in range(counts[i]):
            nums[start] = i
            start += 1

nums = [2,0,2,1,1,0]
print(sortColors(nums))