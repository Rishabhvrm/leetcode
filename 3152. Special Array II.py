from typing import List
class Solution:
    '''
    a number has even parity if it's even and vice versa for odd parity
    '''
    '''
    Brute Force: calculate res for every query
    Time: O(n * q)
    Space: O(1)
    TLE: 523 / 536 
    '''

    def diff_parity(self, a, b):
            if a % 2 and b % 2:                 # both are odd
                return False
            elif a % 2 == 0 and b % 2 == 0:     # both are even
                return False
            else:
                return True

    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        res = []

        for start, end in queries:
            bool_res = True
            for i in range(start, end):
                bool_res = bool_res and self.diff_parity(nums[i], nums[i + 1])
            res.append(bool_res)

        return res
