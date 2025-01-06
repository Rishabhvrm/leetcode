from typing import List

class Solution:
    '''
    1 0 1 1 0
    5 4 3 4 7
    0 0 2 3



    0 0

    1 1

    approach: sum of distance of each "1" from the ith position
    brute force
    time: O(n ** 2)
    '''
    def minOperations(self, boxes: str) -> List[int]:
        res = []
        boxes = [int(b) for b in boxes]

        for i in range(len(boxes)):
            total_dist = 0
            for j in range(len(boxes)):
                if boxes[j] == 1:
                    total_dist += abs(j - i)
            res.append(total_dist)
        
        return res