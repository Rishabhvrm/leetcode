from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        
        ## BRUTE FORCE
        ## T(N): O(N * N)
        ## SPACE: CONSTANT

        # for i in range(l):
        #     for j in range(i+1,l):
        #         if nums[j] == target - nums[i]:
        #             return [i,j]
        # return [] # no solution found

        ## USING HASHMAP/DICTIONARY

        prevMap = {} # val : idx

        for idx, ele in enumerate(nums):
            
            # check if second number exist in dict
            # if yes, return idx for both numbers
            if (target - ele) in prevMap:
                return [prevMap[target - ele], idx]

            # else add ele : idx to dictionary
            prevMap[ele] = idx
        
        return   # no solution
    
    # revisit
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        APPROACH: use dict to store val -> idx
        check if target - val exist in the map
        if it does, return the curr idx and target-val idx
        else add it to the map
        TIME: O(N)
        SPACE: O(1)
        '''

        # { val : idx }
        val_idx_map = {}
        for i, n in enumerate(nums):
            if (target - n) in val_idx_map:
                return [i, val_idx_map[target - n]]
            val_idx_map[n] = i
