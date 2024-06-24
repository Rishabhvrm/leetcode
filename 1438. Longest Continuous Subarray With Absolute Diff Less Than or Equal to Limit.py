from typing import List
import heapq


class Solution:
    '''
    Brute Force: TLE 43 / 61 
    Create every subarray and check if it's valid or not
    valid: abs diff btw max and min < limit
    T(N): O(n ** 3)
    '''
    def abs_diff(self, arr: List[int], limit: int) -> int:
        if (max(arr) - min(arr)) <= limit:
            return True
        return False

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        res = []
        N = len(nums)
        for i in range(N):
            for j in range(i, N):
                if self.abs_diff(nums[i : j + 1], limit):
                    res.append(j - i + 1)

        return max(res)

    '''
    Sliding window brute force
    brute force: for checking max and min
    T(N): O(n ** 2)
    '''
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        l, r = 0, 0
        ans = 0
        min_val, max_val = float('inf'), float('-inf')

        while r < len(nums):
            min_val = min(nums[l : r + 1])
            max_val = max(nums[l : r + 1])
            
            diff = max_val - min_val

            if diff <= limit:
                ans = max(ans, r - l + 1)
                r += 1
            else:
                l += 1

        return ans

    '''
    Approach: Using 2 Heaps + Sliding window
    as long as diff is <= limit, expand
    else shrink
    in a given window you should know what's the max and min val
    use heaps for that
        min_heap will store the min val in the curr_window
        max_heap will store the max val in the curr_window
        pop elements from heap as window shrinks
    
    Time: O(n)
    Space: O(n)
    '''
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        l, r, N = 0, 0, len(nums)
        res = 0
        max_H, min_H = [], []
        top, val, idx = 0, 0, 1

        while r < N:
            heapq.heappush(max_H, [-1 * nums[r], r])
            heapq.heappush(min_H, [nums[r], r])

            # if diff is < limit
            while -1 * max_H[top][val] - min_H[top][val] > limit:
                # shrink => move left
                l = min(max_H[top][idx], min_H[top][idx]) + 1

                # remove elements from heap that are no longer in window
                while min_H[top][idx] < l:
                    heapq.heappop(min_H)
                
                while max_H[top][idx] < l:
                    heapq.heappop(max_H)

            # update res
            res = max(res, r - l + 1)

            # expand => move right
            r += 1

        return res
