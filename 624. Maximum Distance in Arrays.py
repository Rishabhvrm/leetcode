from typing import List
class Solution:
    '''
    Brute force
    '''
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res = 0
        for i in range(len(arrays)):
            min_val = arrays[i][0]
            max_val = arrays[i][-1]
            for j in range(i + 1, len(arrays)):
                max_a_min_b = abs(max_val - arrays[j][0])
                min_a_max_b = abs(min_val - arrays[j][-1])
                diff = max(max_a_min_b, min_a_max_b)
                res = max(res, diff)

        return res 

    '''
    optimized
    '''
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res = 0
        min_val = arrays[0][0]
        max_val = arrays[0][-1]

        for i in range(1, len(arrays)):
            a = abs(max_val - arrays[i][0])
            b = abs(min_val - arrays[i][-1])

            res = max(res, a, b)
            
            max_val = max(max_val, arrays[i][-1])
            min_val = min(min_val, arrays[i][0])

        return res