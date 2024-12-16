import heapq
from typing import List
class Solution:
    '''
    [2,4,1,3,1]
    3
    2
    [4,4,2,3,2]
    '''
    '''
    Approach: using heap as temp DS to find current min val (and idx)
    Time: O(n + k * log n)
    Space: O(n)
    '''
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        res = nums[:]   # creating a copy

        min_h = []
        heapq.heapify(min_h)

        # make heap => [(num, idx)]
        # automatically takes care of picking smaller idx if n is same
        for idx, n in enumerate(nums):
            heapq.heappush(min_h, (n, idx))

        while k:
            num, idx = heapq.heappop(min_h)
            new_num = num * multiplier
            res[idx] = new_num
            heapq.heappush(min_h, (new_num, idx))
            
            k -= 1

        return res