from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:

        ## APPROACH: 2 POINTERS AND L_MAX, R_MAX
        ## T(N): O(N)
        ## Space: O(1)

        left, right = 0, len(height) - 1
        L_max, R_max = height[left], height[right]
        trapped_water = 0

        # notice how idx is not required
        while left < right:
            # can only add in trapped_water if other boundary is greater than current 
            if L_max < R_max:
                left += 1
                L_max = max(L_max, height[left])            # update left_max
                trapped_water += L_max - height[left]
            else:
                right -= 1
                R_max = max(R_max, height[right])
                trapped_water += R_max - height[right]      # update right_max
                
        return trapped_water

height = [0,1,0,2,1,0,1,3,2,1,2,1]
# height = [10,0,0,0] # 0
obj = Solution()
print(obj.trap(height))
