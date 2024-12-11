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

    '''
    Approach-2: Prefix, calculate the res before hand 
    res: till this position how many mismatches have you seen
    given start and end we can find if there are no violating indexes btw them or not
    if prefix[end] - prefix[start] == 0
    Time: O(n)
    Space: O(n)
    '''
    # [a,b,c,d,e]
    # [_,T,F,T,F]
    # 4,3,1,6,2
    # _,T,F,T,F
    # _,0,1,1,2
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        res = []
        prefix = [0] * len(nums)

        for i in range(1, len(nums)): 
            if self.diff_parity(nums[i], nums[i - 1]):
                prefix[i] = prefix[i - 1]
            else:
                prefix[i] = prefix[i - 1] + 1

        for start, end in queries:
            res.append(prefix[end] - prefix[start] == 0)

        return res

