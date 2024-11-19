from typing import List
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:

        def _power(l, r) -> int:
            curr_arr = nums[l : r]
            if any(curr_arr[i + 1] - curr_arr[i] != 1 for i in range(len(curr_arr) - 1)):
                return -1
            # return max(curr_arr)
            return curr_arr[-1]


        res = []
        l, r = 0, k

        while r <= len(nums):
            res.append(_power(l, r))
            l, r = l + 1, r + 1

        return res




















        # l, r = 0, 0
        # max_val = float('-inf')

        # while r < k:
        #     if nums[r] < max_val:
        #         res.append(-1)
        #         break
        #     else:
        #         max_val = nums[r]
        #     r += 1
        # res.append(max_val)
