from typing import List
import heapq
import math
class Solution:
    '''
    approach: simulate using heap
    do below k times:
        take max, perform the operation
        put the res back
    sum up the vals and return
    Time: O(n + k * log n)
    Space: O(n)
    '''
    def pickGifts(self, gifts: List[int], k: int) -> int:
        res = 0
        max_h = []

        # make a max_heap
        for g in gifts:
            heapq.heappush(max_h, -g)

        # perform operation k times
        while k:
            top = -1 * heapq.heappop(max_h)
            updtd_val = math.floor(math.sqrt(top))
            heapq.heappush(max_h, -updtd_val)

            k -= 1

        # calculate sum
        while max_h:
            res += -1 * heapq.heappop(max_h)

        return res