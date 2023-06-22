from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        l = sorted(nums)                        # sort the list

        # subtract 1 from the largest and second largest element in list
        # stored at last and second last index after sorting
        return((l[-1] - 1) * (l[-2] - 1))       

# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/