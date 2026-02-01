from typing import List
class Solution:
    # using sorting
    # T(N): O(n * log n)
    def minimumCost(self, nums: List[int]) -> int:
        a = nums[0]
        new_nums = sorted(nums[1:])
        b, c = new_nums[0], new_nums[1]

        return a + b + c

    # finding min1 and min2
    # T(N): O(n)
    def minimumCost(self, nums: List[int]) -> int:
        min1, min2 = float('inf'), float('inf')

        for x in nums[1:]:
            if x < min1:
                min2 = min1
                min1 = x
            elif x < min2:
                min2 = x
        
        return nums[0] + min1 + min2