from typing import List
class Solution:
    '''
    Brute Force
    '''
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        max_inc, max_dec = 1, 1

        for i in range(N):
            curr_inc = 1
            for j in range(i + 1, N):
                if nums[j] > nums[j - 1]:
                    curr_inc += 1
                else:
                    break
            max_inc = max(max_inc, curr_inc)

        for i in range(N):
            curr_dec = 1
            for j in range(i + 1, N):
                if nums[j] < nums[j - 1]:
                    curr_dec += 1
                else:
                    break
            max_dec = max(max_dec, curr_dec)

        return max(max_inc, max_dec)

    '''
    Single Pass
    '''
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

