from heapq import heapify, heappop, heappush
from typing import List

class Solution:
    '''
    Approach: Brute Force
    Time: O((n ** 2) * log n) 
    Space: O(n ** 2)
    '''
    # def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
    #     subarray_sums = []
    #     res = 0

    #     for i in range(n):
    #         curr_sum = 0
    #         for j in range(i, n):
    #             curr_sum += nums[j]
    #             subarray_sums.append(curr_sum)

    #     subarray_sums.sort()

    #     mod = (10 ** 9) + 7
    #     for i in range(left - 1, right):
    #         res = (res + subarray_sums[i]) % mod

    #     return res

    '''
    Approach: Using heap to get the subarray sums of an array in increasing/decreasing order
    and only take left to right from these subarray sums
    Idea:
    if I could have the subarray sums, I could just take Left to Right from them
    how can I make sure that they are sorted ? => Use a min-heap
    Time: O((n ** 2) * log n) 
    Space: O(n), heap never goes beyond n (every ele will keep on expanding its own subarray)
    '''
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        min_heap = []           # [subarray_sum, end idx of this subarray]
        res, m = 0, (10 ** 9) + 7
        
        heapify(min_heap)
        for i, num in enumerate(nums):          
            heappush(min_heap, [num,i])                 # n * log(n)

        for count in range(1, right + 1):               # 1 to right represents # of subarrays, could be n ** 2 in worst case
            sm, idx = heappop(min_heap)                 # (n ** 2) * log n

            # update res
            if count >= left:
                res = (res + sm) % m

            # push in heap
            new_idx = idx + 1
            if new_idx < n:
                next_pair = [sm + nums[new_idx], new_idx]
                heappush(min_heap, next_pair)
        
        return res