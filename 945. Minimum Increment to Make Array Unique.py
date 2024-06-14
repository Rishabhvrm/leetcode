from typing import List
class Solution:
    '''
    Approach-1: Brute force: sort and check adjacent
    Time: O(n * log n)
    Space: O(1)
    '''
    def minIncrementForUnique(self, nums: List[int]) -> int:
        moves = 0
        nums.sort()

        for i in range(1, len(nums)):
            # duplicate => adjust
            if nums[i - 1] == nums[i]:
                nums[i] += 1
                moves += 1
            
            # if out of order after adjusting
            if nums[i - 1] > nums[i]:
                adjusted_val = nums[i - 1] + 1
                moves += adjusted_val - nums[i]      # order matters here, this line can't be after next line
                nums[i] = adjusted_val

        return moves

    '''
    Approach-2: counting sort, make every occurance 1
    Time: O(n * log n)
    Space: O(1)
    '''
    def minIncrementForUnique(self, nums: List[int]) -> int:
        max_num = max(nums)
        occ = [0] * (max_num + len(nums))   # ** important to realize the size of occ, nums could be [max_v, max_v, max_v]

        # [5, 5, 5], max_v = 5, n = 3
        # 0 1 2 3 4 5 6 7
        # 0 0 0 0 0 3
        # 0 0 0 0 0 1 1 1
    
        moves = 0

        for n in nums:
            occ[n] += 1

        for i, n in enumerate(occ):
            if n > 1:
                steps = n - 1           # steps to reach 1
                occ[i + 1] += steps     # steps to make curr ele diff from prev ele
                moves += steps          

        return moves

