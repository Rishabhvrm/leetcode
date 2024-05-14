'''
You are given a 0-indexed integer array nums.

Swaps of adjacent elements are able to be performed on nums.

A valid array meets the following conditions:

The largest element (any of the largest elements if there are multiple) is at the rightmost position in the array.
The smallest element (any of the smallest elements if there are multiple) is at the leftmost position in the array.
Return the minimum swaps required to make nums a valid array.

 

Example 1:

Input: nums = [3,4,5,5,3,1]
Output: 6
Explanation: Perform the following swaps:
- Swap 1: Swap the 3rd and 4th elements, nums is then [3,4,5,3,5,1].
- Swap 2: Swap the 4th and 5th elements, nums is then [3,4,5,3,1,5].
- Swap 3: Swap the 3rd and 4th elements, nums is then [3,4,5,1,3,5].
- Swap 4: Swap the 2nd and 3rd elements, nums is then [3,4,1,5,3,5].
- Swap 5: Swap the 1st and 2nd elements, nums is then [3,1,4,5,3,5].
- Swap 6: Swap the 0th and 1st elements, nums is then [1,3,4,5,3,5].
It can be shown that 6 swaps is the minimum swaps required to make a valid array.
Example 2:
Input: nums = [9]
Output: 0
Explanation: The array is already valid, so we return 0.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105
'''

'''
case1:
[.. min ........ max ..]

case2:
[.. max ........ min ..]    => one less swap


APPROACH-1: simulate
APPROACH-2: just play with idxes

'''


from typing import List

class Solution:

    def find_max(self, nums: List[int]) -> int:
        max_val = max(nums)
        max_idx = len(nums) - 1 - list(reversed(nums)).index(max_val)
        return max_idx

    def find_min(self, nums: List[int]) -> int:
        min_val = min(nums)
        min_idx = nums.index(min_val)
        return min_idx

    # APPROACH-1: SIMULATE
    def minimumSwaps_1(self, nums: List[int]) -> int:
        swaps = 0
        
        # move max to right end
        max_idx = self.find_max(nums)
        idx = max_idx
        while idx != len(nums) - 1:
            nums[idx], nums[idx + 1] = nums[idx + 1], nums[idx] 
            swaps += 1
            idx += 1

        # move min to left end
        min_idx = self.find_min(nums)
        idx = min_idx
        while idx != 0:
            nums[idx], nums[idx - 1] = nums[idx - 1], nums[idx] 
            swaps += 1
            idx -= 1

        return swaps
    
    # APPROACH-2: PLAY WITH IDXES
    def minimumSwaps_2(self, nums: List[int]) -> int:
        min_idx, max_idx = self.find_min(nums), self.find_max(nums)

        if max_idx < min_idx:
            return min_idx + len(nums) - 1 - max_idx - 1
        else:
            return min_idx + len(nums) - 1 - max_idx

    
# nums = [3,4,5,5,3,1]          # 6
nums = [9]                  # 0
# print(Solution().minimumSwaps_1(nums))
print(Solution().minimumSwaps_2(nums))