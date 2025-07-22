from collections import defaultdict
from typing import List

class Solution:
    # brute force
    # T(N * 2)
    # TLE 58/62
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res = max(nums)

        for i in range(len(nums)):
            unique = set()
            unique.add(nums[i])
            curr_window_sum = nums[i]

            for j in range(i + 1, len(nums)):
                if nums[j] not in unique:
                    unique.add(nums[j])
                    curr_window_sum += nums[j]
                    res = max(res, curr_window_sum)
                else:
                    break
        
        return res

    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res = max(nums)
        freq = defaultdict(int)

        curr_sum, l, r = 0, 0, 0

        while r < len(nums):
            freq[nums[r]] += 1
            curr_sum += nums[r]

            while freq[nums[r]] > 1:
                freq[nums[l]] -= 1
                curr_sum -= nums[l]
                l += 1

            res = max(res, curr_sum)                
            r += 1 

        return res