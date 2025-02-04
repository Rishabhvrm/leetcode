from typing import List
class Solution:
    '''
    
    10,20,30,5,10,50

    T(n): O(N)
    Space: O(1)
    '''
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = nums[0]
        curr_sum = res

        for i in range(len(nums) - 1):
            if nums[i + 1] > nums[i]:               # if ascending, add to prev sum
                curr_sum += nums[i + 1]
            else:                                   # if dip, reset sum to new val
                curr_sum = nums[i + 1]

            res = max(res, curr_sum)
        
        return res