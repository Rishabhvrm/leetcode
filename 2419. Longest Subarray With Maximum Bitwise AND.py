from typing import List
class Solution:
    '''
    Check all subarrays
    TLE
    '''
    def longestSubarray(self, nums: List[int]) -> int:
        max_len = 0
        max_val = float('-inf')
        for i in range(len(nums)):
            val = nums[i]
            for j in range(i, len(nums)):
                val &= nums[j]
                if val > max_val:
                    max_val = val
                    max_len = j - i + 1
                elif val == max_val:
                    max_len = max(max_len, j - i + 1)
                    

        return max_len


    '''
    Observation: AND of 2 numbers would never be greater than the numbers involved
    hence, look for the largest number (or a streak of largest numbers)
    question reduces to: Longest Sub Array having max value
    2 pass, look for max val
    '''
    def longestSubarray(self, nums: List[int]) -> int:
        target = max(nums)
        streak, res = 0, 0

        for n in nums:
            if n == target:
                streak += 1
            else:
                streak = 0
            res = max(res, streak)

        return res

    '''
    same as above, just
    one-pass
    '''
    def longestSubarray(self, nums: List[int]) -> int:
        max_val, streak, res = 0, 0, 0

        for n in nums:
            if n > max_val:
                max_val = n
                res = 0
                streak = 0
            
            if n == max_val:
                streak += 1
            else:
                streak = 0

            res = max(res, streak)

        return res