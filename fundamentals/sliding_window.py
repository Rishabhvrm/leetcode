# Given an array of integers, we want to find the maximum sum of any contiguous subarray of a specified size k.
import collections

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

def max_subarray_sum2(nums, k) -> int:
    l, r = 0, k
    curr_sum = sum(nums[:k])
    max_sum = curr_sum

    while r < len(nums):
        curr_sum -= nums[l]
        curr_sum += nums[r]
        max_sum = max(max_sum, curr_sum)
        l, r = l + 1, r + 1

    return max_sum
nums = [1,2,3,4,5,6]
print(max_subarray_sum2(nums, 3))

def max_subarray_sum2_D(nums, k) -> int:
    window = collections.deque()

    for i in range(k):
        window.append(nums[i])

    curr_sum = max_sum = sum(window)

    while i < len(nums):
        curr_sum -= window.popleft()
        curr_sum += nums[i]
        window.append(nums[i])
        max_sum = max(max_sum, curr_sum)
        i += 1

    return max_sum
nums = [1,2,3,4,5,6]
print(max_subarray_sum2_D(nums, 3))


def revisit_sliding_window(nums, k) -> int:
    if k > len(nums):
        return nums

    max_sum = 0
    curr_sum = sum(nums[:k])
    #  i = [0,1,2]
    for i in range(len(nums) - k):
        curr_sum -= nums[i]
        curr_sum += nums[i + k]
        max_sum = max(max_sum, curr_sum)

    return max_sum
    #   0 1 2 3 4 5
nums = [1,2,3,4,5,6]
print(revisit_sliding_window(nums, 3))
