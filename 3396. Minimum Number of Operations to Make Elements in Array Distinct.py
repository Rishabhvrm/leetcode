import math
from typing import List
class Solution:
    '''
                    #
    1,2,3,4,2,3,3,5,7
    
    1,2,3,4,2,3,3,5,7,3,3
    
    '''
    # def minimumOperations(self, nums: List[int]) -> int:
    #     s = set()
    #     i, j = 0, 0
    #     counter = 0

    #     while i < len(nums):
    #         if nums[i] in s:
    #             j += 3
    #             i = j
    #             s = set()
    #             counter += 1
    #         else:
    #             s.add(nums[i])
    #             i += 1
        
    #     return counter


    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        s = set()

        for i in range(n - 1, -1, -1):
            if nums[i] in s:
                return math.ceil((i + 1)/3)
            else:
                s.add(nums[i])

        return 0