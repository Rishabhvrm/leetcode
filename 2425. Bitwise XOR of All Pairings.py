from typing import List
class Solution:
    '''
    brute force
    Time: O(n * m), n: len of nums1, m: len of nums2
    TLE 37/42
    '''
    # def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
    #     res = 0

    #     for a in nums1:
    #         for b in nums2:
    #             res ^= a ^ b

    #     return res



    '''
    a b c       1 2 3 4
    a1 a2 a3 a4 b1 b2 b3 c1 c2 c3 c4
    (a^1)^(a^2) == a ^ 1 ^ a ^ 2
    XOR is cummutative (order of operations doesn't matter)


    '''
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0

        # if len of any array is even, the other array will just turn into 0
        # since a ^ a = 0
        # hence only calculate for the odd len

        if len(nums2) % 2:
            for n in nums1:
                res ^= n

        if len(nums1) % 2:
            for n in nums2:
                res ^= n

        return res