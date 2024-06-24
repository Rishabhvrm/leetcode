from typing import List
from collections import deque

class Solution:
    '''
    Approach: Brute force + sliding window
    If L is 1, skip => Shrink
    If L is 0, flip the next k elements => Expand
        
    TLE : 89 / 113
    Time: O(n * k)
    Space: O(1)
    '''
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        steps = 0
        l, r = 0, 0
       
        while r < len(nums):
            if nums[l] == 0:
                r = l

                # out of bound
                if l + k - 1 >= len(nums):
                    return -1
                
                while r <= l + k - 1:
                    nums[r] = 0 if nums[r] else 1
                    r += 1
                    steps += 1
            l += 1
            r = l
        
        return (steps // k)

    '''
    Approach: flip_counts_for_current_i and idx for where did you apply the flip
    Time: O(n)
    Space: 
        O(n) if used a data-structure, could be set/map/array
        O(1) if modified I/P
    '''
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        # flip_idx_set = set()  # use this if i/p modification is not allowed
        i, fcount_for_i, steps, N = 0, 0, 0, len(nums)

        while i < N:
            # check if flip count is valid for this i or not
            # if i >= k and (i - k) in flip_idx_set: # use this if i/p modification is not allowed
            if i >= k and nums[i - k] == -1:    # marking
                fcount_for_i -= 1

            # flip
            if fcount_for_i % 2 == nums[i]:
                
                # will check out of bounds only if I want to flip the next k vals
                if i + k - 1 >= N:
                    return -1

                steps += 1
                # flip_idx_set.add(i)   # use this if i/p modification is not allowed
                nums[i] = -1            # marking, modifying the I/P
                fcount_for_i += 1
            
            i += 1
        
        return steps


    '''
    Approach: Using a deque of size k to keep history of flips
    same as above, just less space
    Time: O(n)
    Space: O(k)
    '''
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        # flip_idx_set = set()  # use this if i/p modification is not allowed
        i, fcount_for_i, steps, N = 0, 0, 0, len(nums)
        flip_history_Q = deque() # will be of size window i.e k

        for i in range(N):
            # check if flip count is valid for this i or not
            if i >= k:
                fcount_for_i -= flip_history_Q.popleft()

            # flip
            if fcount_for_i % 2 == nums[i]:
                
                # will check out of bounds only if I want to flip the next k vals
                if i + k - 1 >= N:
                    return -1

                steps += 1
                flip_history_Q.append(1) # 1 means I've applied flip at idx i
                fcount_for_i += 1
            else:
                flip_history_Q.append(0) # 0 means I've not applied flip at idx i
            
        
        return steps
