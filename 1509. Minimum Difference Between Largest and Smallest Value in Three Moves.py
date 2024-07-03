import heapq
from typing import List
'''
window movement, everything else will be in the window 
except below
get the min and max from the window

I can skip 3 from right
I can skip 1 from left and 2 from right
I can skip 2 from left and 1 from right
I can skip 3 from left
'''
class Solution:
    '''
    #  #  #  # 
       #  #  #  # 
          #  #  #  #
             #  #  #  #
    10 19 31 48 48 81 92
    Approach-1: Sliding-window (only 4 sliding windows), pick max/min in window
    T(N): O(n * log n), sorting
    Space: O(1)
    '''
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0

        nums.sort()

        l, r = 0, len(nums) - 4
        ans = float('inf')

        while r < len(nums):
            ans = min(ans, nums[r] - nums[l])
            l, r = l + 1, r + 1

        return ans
    
    '''
    Approach-2: using heaps, take the 4 min and 4 max elements and check their difference
    refrence: https://www.youtube.com/watch?v=S6cUjbQuTnE
    T(N): O(n)
    Space: O(n)
    '''
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0

        min_4 = sorted(heapq.nsmallest(4, nums))
        max_4 = sorted(heapq.nlargest(4, nums))
        res = float('inf')

        for i in range(4):
            res = min(res, max_4[i] - min_4[i])

        return res