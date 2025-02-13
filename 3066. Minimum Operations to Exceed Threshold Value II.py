import heapq
from typing import List
class Solution:
    '''
    [2,11,10,1,3], k = 10
    
    1 * 2 + 2 => 4
    3 * 2 + 4 => 10

    [1,1,2,4,9], k = 20

    1 * 2 + 1 => 3
    2,3,4,9
    2 * 2 + 3 => 7
    4,7,9
    4 * 2 + 7 => 15
    9,15
    9 * 2 + 15 => 33


    '''
    def minOperations(self, nums: List[int], k: int) -> int:
        min_heap = []
        heapq.heapify(min_heap)

        for n in nums:
            heapq.heappush(min_heap, n)

        counter = 0
        while True:
            x = heapq.heappop(min_heap)
            if x >= k:
                break
            y = heapq.heappop(min_heap)

            new_val = (min(x, y) * 2) + max(x, y)
            heapq.heappush(min_heap, new_val)
            counter += 1


        return counter