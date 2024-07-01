from typing import List
class Solution:
    '''
    Approach: Sliding window
    Time: O(N)
    Space: O(1)
    '''
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        l, r = 0, 0

        while r < len(arr):
            if not arr[r] % 2:
                l = r + 1
            if r - l + 1 == 3:
                return True
            r += 1
        
        return False
    
    '''
    Approach: odd count
    Time: O(N)
    Space: O(1)
    '''
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        c_odd_count = 0

        for ele in arr:
            if ele % 2:
                c_odd_count += 1
            else:                       # reset if even
                c_odd_count = 0

            if c_odd_count == 3:
                return True

        return False

    '''
    Approach: chec if product is odd
    Time: O(N)
    Space: O(1)
    '''
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr) - 2):
            if arr[i] * arr[i + 1] * arr[i + 2] % 2:
                return True

        return False