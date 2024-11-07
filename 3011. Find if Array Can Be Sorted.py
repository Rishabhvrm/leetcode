from typing import List
class Solution:
    '''
    Approach: Bubble sort
    Time: O(N ** 2)
    Space: O(1)
    '''
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(n - i - 1):
                if nums[j] <= nums[j + 1]:
                    continue

                if bin(nums[j]).count("1") == bin(nums[j + 1]).count("1"):
                    # swap
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                else:
                    # adjacent numbers are not in order and they can't be swapped
                    return False
        
        return True


    '''
    Approach: Split into segments and check boundaries (max and min in each segment)
    using hints
    Time: O(N)
    Space: O(1)
    '''
    def canSortArray(self, nums: List[int]) -> bool:
        def count_bits(n):
            return bin(n).count("1")

        curr_min, curr_max = nums[0], nums[0]
        prev_max = float('-inf')

        for n in nums:
            if count_bits(n) == count_bits(curr_max):
                curr_min = min(curr_min, n)
                curr_max = max(curr_max, n)
            else:
                if curr_min < prev_max:
                    return False
                prev_max = curr_max
                curr_min, curr_max = n, n

            # check last group
            if curr_min < prev_max:
                return False

        return True
                




















    