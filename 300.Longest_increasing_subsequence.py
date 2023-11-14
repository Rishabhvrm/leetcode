from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        ## APPROACH: DP
        ## traverse in reverse, check if n[j] > n[i] then update LIS[i]
        ## TIME: O( n * n )
        ## SPACE: O( n )

        l = len(nums)
        LIS = [1] * l

        for i in range(l - 1, -1, -1):
            for j in range(i + 1, l):
                if nums[j] > nums[i]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        return max(LIS)
    

nums1 = [10,9,2,5,3,7,101,18]
nums2 = [0,1,0,3,2,3]
nums3 = [7,7,7,7,7,7,7]
obj = Solution()

print(obj.lengthOfLIS(nums1))
print(obj.lengthOfLIS(nums2))
print(obj.lengthOfLIS(nums3))