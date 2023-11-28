from typing import List
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_dist, min_idx = float('inf'), -1

        for i, (a, b) in enumerate(points):
            # check point validity
            if a == x or b == y:
                dist = abs(a - x) + abs(b - y)          # calculate Manhattan distance
                if dist < min_dist:                     # update values if found new dist
                    min_dist, min_idx = dist, i
        
        return min_idx


obj = Solution()
x = 3
y = 4
points = [[1,2],[3,1],[2,4],[2,3],[4,4]]

x = 3
y = 4
points = [[3,4]]

x = 3
y = 4
points = [[2,3]]
print(obj.nearestValidPoint(x,y,points))