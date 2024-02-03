from typing import List

# EASY
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        ## APPROACH: Brute Force
        ## TIME: O(n * n)
        ## Space: O(1)
        
        counter, l = 0, len(nums)

        for i in range(l):
            for j in range(i + 1, l):
                if abs(nums[i] - nums[j]) == k: counter += 1

        return counter
        


obj = Solution()

nums, k = [1,2,2,1], 1  # o/p = 4
# nums, k = [1,3], 3      # o/p = 0
# nums, k = [2,2,3,1], 1  # o/p = 4

print(obj.countKDifference(nums, k))