from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:

        ## APPROACH: use house robber 1 on nums[1:] and nums[:-1]
        ## TIME: O(N)
        ## SPACE: O(1)

        def helper(nums):
            rob1, rob2 = 0, 0

            # [..., rob1, rob2, n, n+1, ... ]
            for n in nums:
                rob_max = max(n + rob1, rob2)
                rob1 = rob2
                rob2 = rob_max

            return rob2

        # if only 1 value in input, skip first value, skip last value
        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))
    

    '''
    Recursion
    # TLE 53/75
    '''
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def house_robber_1(arr):

            def solve(idx):
                if idx >= len(arr):
                    return 0

                steal = arr[idx] + solve(idx + 2)
                dont_steal = solve(idx + 1)
                return max(steal, dont_steal)

            return solve(0)

        n = len(nums)
        return max(house_robber_1(nums[0: n - 1]), house_robber_1(nums[1: n]))

    '''
    Top-down memoization
    '''
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def house_robber_1(arr: List[int]) -> int:
            def solve(idx):
                if idx >= len(arr):
                    return 0
                
                if idx in memo:
                    return memo[idx]

                steal = arr[idx] + solve(idx + 2)
                skip = solve(idx + 1)
                memo[idx] = max(steal, skip)
                return memo[idx]
            
            memo = {}           # ith house: max money till this house
            return solve(0)
        
        n = len(nums)
        return max(house_robber_1(nums[0 : n - 1]), house_robber_1(nums[1 : n]))

    '''
    Bottom-up:
    Defining State:
    dp[i] = Profit when we're done with i houses
    '''
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        def house_robber_1(arr: List[int]) -> int:
            dp = [0 for _ in range(len(arr))]
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])

            for i in range(2, len(arr)):
                steal = arr[i] + dp[i - 2]
                skip = dp[i - 1]
                dp[i] = max(steal, skip)
            
            return dp[-1]

        n = len(nums)
        return max(house_robber_1(nums[: n - 1]), house_robber_1(nums[1:n]))