from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        # traverse array backwards
        for i in range(len(nums) - 2, -1, -1):
            # if I can reach goal from i
            # move goal at i
            if i + nums[i] >= goal:
                goal = i
        
        # goal should be moved to all the way to first position
        # if not return False
        return goal == 0
