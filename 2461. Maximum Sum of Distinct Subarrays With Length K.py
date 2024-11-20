from typing import List
from collections import defaultdict
class Solution:
    """   ___
    7 9 9 2 9

    Approach: Sliding window with hashmap for count
    Time: O(N)
    Space: O(K), at a given time there'll be at most k elements in the dict
    """
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        curr_sum, max_sum = 0, 0
        freq = defaultdict(int)
        
        # move k steps => expand the window
        while r < k:
            curr_sum += nums[r]
            max_sum = max(max_sum, curr_sum)
            freq[nums[r]] += 1
            r += 1

        if len(freq.keys()) != k:
            max_sum = 0
            
        # slide the window
        while r < len(nums):
            curr_sum -= nums[l]
            freq[nums[l]] -= 1
            
            if freq[nums[l]] == 0:
                freq.pop(nums[l])
            
            l += 1

            curr_sum += nums[r]
            freq[nums[r]] += 1

            if len(freq) == k and r - l + 1 == k:
                max_sum = max(max_sum, curr_sum)
                
            r += 1

        return max_sum

