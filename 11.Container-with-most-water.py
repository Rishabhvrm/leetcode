from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ## APPROACH: MOVE POINTERS, START AND END
        ## TIME: O(n)
        ## SPACE: O(1)

        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            curr_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, curr_area)

            # move pointers based on whichever height is smaller
            # in the hope that you'll find bigger height next
            if height[left] < height[right]: left += 1
            else: right -= 1
        
        return max_area
    
height = [1,8,6,2,5,4,8,3,7]
# height = [1,1]
obj = Solution()
print(obj.maxArea(height))