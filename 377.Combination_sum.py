from typing import List
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        ## APPROACH-1: BRUTE FORCE
        ## TIME: O(n ^ target), at each level you have n choices, 
        ## and max level could be = target (1,1,1,1) for 4
        ## SPACE: O(n)
        '''
        def bactrack(idx, curr_sum, combinations):
            if curr_sum > target: return

            if curr_sum == target:
                res.append(combinations.copy())
                return
            
            for idx in range(len(nums)):
                curr_sum += nums[idx]
                combinations.append(nums[idx])
                bactrack(idx, curr_sum, combinations)
                curr_sum -= nums[idx]
                combinations.pop()

        res = []
        bactrack(0, 0, [])
        return len(res)
        '''

        ## APPROACH-2: DP
        n = len(nums)

        dp = [0] * (target + 1)
        dp[0] = 1       # There is one combination for target value 0, which is an empty set

        for t in range(1, target + 1):
            # this is the branching
            # visiting 1 branch at a time
            # dp[n] = dp[target - n1] + dp[target - n2] + dp[target - n3]
            # where n1, n2, n3 are elements of nums
            for n in nums:
                if t - n >= 0: dp[t] += dp[t - n]

        return dp[target] 


# Example usage:
nums = [1, 2, 3]
target = 4
obj = Solution()
print(obj.combinationSum4(nums, target))