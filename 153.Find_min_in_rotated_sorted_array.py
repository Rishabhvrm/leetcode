from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        ## APPROACH-1: USING IN-BUILT FUNCTION
        ## TIME: O(N), NOT VALID HERE
        ## SPACE: O(1)

        # return min(nums)

        ## APPROACH-2: MODIFIED BINARY SEARCH (CZ SORTED), HINT- SORTED ARRAY
        ## TIME: O(log N)
        ## SPACE: O(1)
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            # val(mid) < val(right), min should lie in first half, move right pointer
            if nums[mid] <= nums[right]:
                right = mid
            # val(mid) > val(right), min should lie in second half, move left pointer
            elif nums[mid] > nums[right]:
                left = mid + 1
                
        # could return nums[right] as well
        return nums[left]
    
nums = [5,1,2,3,4]

s = Solution()
print(s.findMin(nums))
