from typing import List

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        '''
        Approach: prefix sum
        find min value among the prefix sum arr
        Time: O(n)
        Space: O(1)
        '''
        min_val = 0      # it will stay 0 if all values in nums are +ve
        prefix_sum = 0

        for n in nums:
            prefix_sum += n
            min_val = min(min_val, prefix_sum)
            
        # so that step by step is never less than 1
        return 1 + abs(min_val)
    
obj = Solution()
nums = [-3,2,-3,4,2]        # 5
# nums = [1,2]              # 1
# nums = [1,-2,-3]          # 5
# nums = [-3,-2,1]          # 6
print(obj.minStartValue(nums))