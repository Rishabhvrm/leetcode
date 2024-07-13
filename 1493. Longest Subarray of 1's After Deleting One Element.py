from typing import List
class Solution:
    '''
      L
    0,1,1,1,0,1,1,0,1
                    R

    keep curr count of 0

    '''
    '''
    Instead of deleted one element, let's see this as at most one zero is allowed
    Approach: Brute Force Sliding window: Make every subarray, see if allows for one 0, break for 2 or more
    calculate len of window at every step

    TLE at 67 / 82
    T(N): O(n ** 2)
    Space: O(1)
    '''
    def longestSubarray(self, nums: List[int]) -> int:
        max_size, N = 0, len(nums)

        for i in range(N):
            zero_count = 0
            for j in range(i, N):
                if nums[j] == 0:
                    zero_count += 1

                if zero_count > 1:
                    break

                max_size = max(max_size, j - i + 1)
        
        return max_size - 1

    '''
    Approach: Sliding window optimized
    T(N): O(n)
    Space: O(1)

            L
    0,1,1,1,0,1,1,0,1
                  R
    '''
    def longestSubarray(self, nums: List[int]) -> int:
        zero_count, L, R, N = 0, 0, 0, len(nums)
        max_size = 0

        while R < N:
            if nums[R] == 0:
                zero_count += 1
            
            # move L until there is only 1 zero in the curr_window
            # decrement zero_count along the way
            while zero_count > 1:
                if nums[L] == 0: 
                    zero_count -= 1
                L += 1

            max_size = max(max_size, R - L + 1)
            R += 1
        
        return max_size - 1
