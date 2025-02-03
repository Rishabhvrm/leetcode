from typing import List
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res, curr_inc, curr_dec = 1, 1, 1

        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] > 0:
                curr_inc += 1
                curr_dec = 1
            elif nums[i + 1] - nums[i] < 0:
                curr_dec += 1
                curr_inc = 1
            elif nums[i + 1] == nums[i]:
                curr_inc = curr_dec = 1
            res = max(res, curr_inc, curr_dec)

        return res