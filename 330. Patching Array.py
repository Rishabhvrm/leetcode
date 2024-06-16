from typing import List
class Solution:
    '''
    Time: O (max(len(nums), log(target)))
    Reference: https://www.youtube.com/watch?v=K2IomuIFbPg
    '''
    def minPatches(self, nums: List[int], n: int) -> int:
        patches, max_reachable, i = 0, 0, 0

        while max_reachable < n:
            if i < len(nums) and nums[i] <= (max_reachable + 1):
                max_reachable += nums[i]
                i += 1
            else:
                max_reachable += (max_reachable + 1)
                patches += 1                

        return patches

    '''
             *
        [1,5,10], n = 20

        [0,0]
        [0,1] => 1 + 2
        [0,3] => 3 + 4
        [0,7] => 7 + 5
        [0,12]
    '''