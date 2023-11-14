from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums) # can't initialize to 0 bcz what if nums = [-1]
        curr_max, curr_min = 1, 1
        
        for n in nums:
            last_curr_max = curr_max
            curr_max = max( n * curr_max, n * curr_min, n )         # [-1, 8]
            curr_min = min( n * last_curr_max, n * curr_min, n )    # [-1, -8]
            res = max( curr_max, res )
        return res
    
    ## REVISIT
    ## APPROACH: keep track of max and min at each step
    # and calculate the next max based on that
    # similar to 53. max sum subarray, kadane's variation

    ## TIME: O(n)
    ## SPACE: O(1)
    def maxProduct2(self, nums):
        max_prod, curr_max, curr_min = nums[0], 1, 1
        for n in nums:
            prev_curr_max = curr_max
            curr_max = max(curr_min * n, curr_max * n, n)
            curr_min = min(curr_min * n, prev_curr_max * n, n)
            max_prod = max(max_prod, curr_max)
        return max_prod       
    
obj = Solution()
nums=[2,3,-2,4]
nums = [-2, 0, -1]
nums = [-1, 8]
nums = [1, -8]
print(obj.maxProduct2(nums))