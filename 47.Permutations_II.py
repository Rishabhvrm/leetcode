from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        ## APPROACH-1: similar to 46. Permutations, just check before adding to result
        ## TIME: O(N * N!)
        ## SPACE: O(N!)

        # def backtrack(first):
        #     # base case
        #     if first == n:
        #         if nums not in res:
        #             res.append(nums[:])
        #         return

        #     for idx in range(first, n):
        #         # swap
        #         nums[first], nums[idx] = nums[idx], nums[first]
        #         # recursively generate permutations
        #         backtrack(first + 1)
        #         # backtrack the swap
        #         nums[first], nums[idx] = nums[idx], nums[first]


        ## APPROACH-2: same as above, use a set to keep track of duplicates
        def backtrack(first):
            # base case
            if first == n:
                res.append(nums[:])
                return

            # use set to store duplicates
            used = set()

            for idx in range(first, n):
                if nums[idx] not in used:                    
                    used.add(nums[idx]) 
                    # swap
                    nums[first], nums[idx] = nums[idx], nums[first]
                    # recursively generate permutations
                    backtrack(first + 1)
                    # backtrack the swap
                    nums[first], nums[idx] = nums[idx], nums[first]

        res = []
        n = len(nums)
        backtrack(0)
        return res