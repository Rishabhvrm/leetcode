from typing import List
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        curr_num = 0
        i = 0
        res = []

        while i < len(nums):
            curr_num = 2 * curr_num + nums[i]
            if curr_num % 5 == 0:
                res.append(True)
            else:
                res.append(False)
            i += 1

        return res

    def cleanerCode(nums: List[int]) -> List[bool]:
        curr_num = 0
        res = []
        
        for n in nums:
            curr_num = (2 * curr_num) + n
            res.append(curr_num % 5 == 0)

        return res