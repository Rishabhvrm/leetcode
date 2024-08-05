from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        # [..., rob1, rob2, n, n+1, ... ]
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2
    
    
    '''
    Recursion
    48 / 70 TLE
    '''
    def rob(self, nums: List[int]) -> int:
        
        def calc(arr):
            if len(arr) == 0:
                return 0
            
            temp = max(arr[0] + calc(arr[2:]), calc(arr[1:]))
            possible_robbery_sum.append(temp)

            return possible_robbery_sum[-1]

        possible_robbery_sum = []
        calc(nums)
        # print(possible_robbery_sum)
        return max(possible_robbery_sum)

    '''
    Top-down memo
    '''
    def rob(self, nums: List[int]) -> int:
            def calc(arr):
                if len(arr) == 0:
                    return 0
                
                if tuple(arr) in memo:
                    return memo[tuple(arr)]
                else:
                    temp = max(arr[0] + calc(arr[2:]), calc(arr[1:]))
                    possible_robbery_sum.append(temp)
                    memo[tuple(arr)] = temp

                return possible_robbery_sum[-1]

            possible_robbery_sum = []
            memo = {}       # arr: robbery_amt
            calc(nums)
            return max(possible_robbery_sum)

    '''
    Bottom-up
    '''
    def rob(self, nums: List[int]) -> int:        
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums)

        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        
        return dp[-1]

    '''
    top-down memoization
    '''
    def solve(self, nums: List[int], idx: int) -> int:
        if idx >= len(nums):
            return 0

        if idx in self.memo:
            return self.memo[idx]

        steal = nums[idx] + self.solve(nums, idx + 2)     # steal this house and skip the next
        skip = self.solve(nums, idx + 1)                  # skip this house and move to next
        self.memo[idx] = max(steal, skip)
        return self.memo[idx]

    def rob(self, nums: List[int]) -> int:   
        self.memo = {}       # idx: max I can steal when I'm standing here     
        return self.solve(nums, 0)

    '''
    bottom-up
    Defining a state: 
    dp[i] : max stolen money till house i
    which is:
        steal: money at this house + money till i - 2 th house 
        don't steal: money I've till i - 1 th house
    '''
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]   
        dp = [0 for _ in range(len(nums))]
        
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            steal = nums[i] + dp[i - 2]         # take current and skip adjacent
            dont_steal = dp[i - 1]              # skip current and take the adjacent
            dp[i] = max(steal, dont_steal)

        return dp[len(nums) - 1]
        # return dp[-1]