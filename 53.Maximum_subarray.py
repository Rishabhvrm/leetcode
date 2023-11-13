from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        
        ## APPROACH-1: check every subarray and pick max sum
        ## TIME: O( n * n )
        ## SPACE: O(1)
        # l = len(nums)
        # max_sum = nums[0]
        # for i in range(l):
        #     curr_sum = 0
        #     for j in range(i, l):
        #         curr_sum += nums[j]
        #         max_sum = max(max_sum, curr_sum)

        # return max_sum


        ## APPROACH-2: kadane's algorithm
        ## TIME: O(n)
        ## SPACE: O(1)
        max_sum, curr_sum = nums[0], 0

        for n in nums:
            curr_sum = max(n + curr_sum, n)
            max_sum = max(max_sum, curr_sum)
        
        return max_sum




nums = [-2,1,-3,4,-1,2,1,-5,4]
# curr_sum = [-2,1,-2,4,3,5,6,1,5]
obj = Solution()
print(obj.maxSubArray(nums))
