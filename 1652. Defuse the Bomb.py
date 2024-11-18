from typing import List
class Solution:
    '''
    Approach: Brute force, simulate
    sign of k determines direction
    magnitude of k determines steps to take

    if -ve, reverse the array and reverse the ans
    2,4,9,3
    3,9,4,2
    13,6,5,12
    '''
    def decrypt(self, code: List[int], k: int) -> List[int]:
        l = len(code)

        if k < 0:
            code = code[::-1]
        
        if k == 0:
            return [0] * l

        res = []

        for i in range(l):
            count = 1
            curr_ele = 0
            while count <= abs(k):
                curr_ele += code[(i + count) % l]
                count += 1
            res.append(curr_ele)

        return res[::-1] if k < 0 else res