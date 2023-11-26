from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        ## APPROACH: use cloud boundary concept to move all vals to end of array
        ## TIME: O( n ), traversing backwards
        ## SPACE: O( 1 )
        n = len(nums)
        boundary, count = n - 1, 0

        for i in range(n - 1, -1, -1):
            if nums[i] == nums[val]:
                nums[i], nums[boundary] = nums[boundary], nums[i]
                boundary -= 1
                count += 1
        
        return n - count