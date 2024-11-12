from typing import List
class Solution:
    '''
    Brute Force: Check every subarray
    correct but TLE
    T(N): O(N ** 2)
    '''
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        res = float('inf')
        
        for i in range(len(nums)):
            curr_OR = nums[i]
            for j in range(i, len(nums)):
                curr_OR |= nums[j]
                if curr_OR >= k:
                    res = min(res, j - i + 1)

        return -1 if res == float('inf') else res

    '''
    Optimized: Sliding window, 32 bit array (increment count to set bits)
    to shrink the window = to undo the OR operation = decrement the count 
    arr[i] represents how many times the ith bit has been set
    while shrinking, decrement all the idxes which are present in the number
    which we are leaving behind
    T(N): O(N)
    '''
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:

        res = float('inf')
        l, r = 0, 0
        bits = [0] * 32


        def update_bits_arr(n, diff):
            for i in range(32):
                if n & (1 << i):
                    bits[i] += diff

        def bits_to_int(bits):
            num = 0
            for i in range(32):
                if bits[i]:
                    # num += (2 ** i)
                    num += (1 << i)
            return num

        while r < len(nums):
            # expand window => increment count for set bits
            update_bits_arr(nums[r], 1)
            curr_or = bits_to_int(bits)


            while l <= r and curr_or >= k:
                res = min(res, r - l + 1)
                # shrink window => decrement count for set bits
                update_bits_arr(nums[l], -1)
                curr_or = bits_to_int(bits)
                l += 1

            r += 1



        return -1 if res == float('inf') else res