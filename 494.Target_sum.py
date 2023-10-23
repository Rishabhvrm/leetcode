from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        ## APPROACH-1: BACKTRACKING, DECISION TREE
        ## TIME: O(2 ^ N), at every point we have 2 choice, traverse whole array of size N
        ## SPACE: no extra space, just recursion stack
        ## Gives TLE
        # def backtrack(idx, curr_sum):
        #     # base case
        #     if idx == len(nums):
        #         return 1 if curr_sum == target else 0

        #     else:
        #         add = backtrack(idx + 1, curr_sum + nums[idx])
        #         subtract = backtrack(idx + 1, curr_sum - nums[idx])
        #         return add + subtract    
        
        # return backtrack(0, 0)
        
        ## APPROACH-2: DP
        ## TIME: O(N * T)
        ## SPACE: O(N * T) dictionary, and recursion stack, could be right

        def backtrack(idx, curr_sum):
            # base case
            if idx == len(nums):
                return 1 if curr_sum == target else 0
            if (idx, curr_sum) in dp:
                return dp[(idx, curr_sum)]
            
            dp[(idx, curr_sum)] = (backtrack(idx + 1, curr_sum + nums[idx]) + 
                                   backtrack(idx + 1, curr_sum - nums[idx]))
            return dp[(idx, curr_sum)]

        # (index, total) -> # of ways
        dp = {} 
        return backtrack(0, 0)

nums = [1,1,1,1,1]
target = 3
s = Solution()
print(s.findTargetSumWays(nums, target))
