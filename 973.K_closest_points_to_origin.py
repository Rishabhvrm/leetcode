from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        ## APPROACH: CALCULATE DISTANCE, 
        ## ADD DISTANCE TO LIST, 
        ## ADD LIST TO HEAP, 
        ## TAKE OUT TOP K TIMES

        min_heap = []

        # add distances to heap
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            min_heap.append([dist, x, y])

        # sort/heapify
        heapq.heapify(min_heap)

        res = []
        # take out the top points k times
        for _ in range(k):
            res.append(heapq.heappop(min_heap)[1:])

        return res
    
points = [[3,3],[5,-1],[-2,4]]
k = 2
obj = Solution()
print(obj.kClosest(points, k))