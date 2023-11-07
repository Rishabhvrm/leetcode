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
       