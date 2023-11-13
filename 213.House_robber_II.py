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