# Given an array of integers, we want to find the maximum sum of any contiguous subarray of a specified size k.

def max_subarray_sum(nums, k) -> int:
    if k > len(nums):
        return -1
    
    max_sum = float("-infinity")
    curr_sum = sum(nums[:k])

    for idx in range(len(nums) - k):
        curr_sum -= nums[idx]
        curr_sum += nums[idx + k]
        max_sum = max(max_sum, curr_sum)

    return max_sum

nums = [1,2,3,4,5,6]
print(max_subarray_sum(nums, 3))