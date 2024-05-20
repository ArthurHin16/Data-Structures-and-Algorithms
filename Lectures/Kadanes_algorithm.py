"""
Kadane´s algorithm helps us to find the contigous subarray with at least one element, which has the largest sum. 
"""
def kadanes_algorithm(nums):
    curr_sum = nums[0]
    max_sum = nums[0]
    for num in nums:        
        curr_sum = max(curr_sum + num, num)
        if curr_sum > max_sum:
            max_sum = curr_sum
    return max_sum

def kadanes_contigous_array(nums):
    curr_sum = nums[0]
    max_sum = nums[0]
    start = 0
    temp_start = 0
    end = 0
    for i in range(len(nums)):
        if curr_sum + nums[i] > nums[i]:
            curr_sum += nums[i]
        else:
            curr_sum = nums[i]
            temp_start =  i
        if curr_sum > max_sum:
            max_sum = curr_sum
            start = temp_start
            end = i
    print(nums[start:end + 1])
    return max_sum




nums = [-2,1,-3,4,-1,2,1,-5,4]
print(kadanes_algorithm(nums))
# Expected output: 6

print(kadanes_contigous_array(nums))