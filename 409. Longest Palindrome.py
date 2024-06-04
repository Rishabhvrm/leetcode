from collections import defaultdict
class Solution:
    '''
    Approach: Using Hash Map
    T(n): O(n)
    Space: O(n)
    '''
    def longestPalindrome(self, s: str) -> int:
        char_occ = defaultdict(int)
        for char in s:
            char_occ[char] += 1
        
        res = 0
        odd = False
        for k, v in char_occ.items():
            if v % 2:
                odd = True
                res += v - 1
            else:
                res += v
        
        return res + 1 if odd else res

    '''
    Approach: Using Hash Set
    T(n): O(n)
    Space: O(n)
    '''
    def longestPalindrome(self, s: str) -> int:
        char_set = set()
        res = 0

        for char in s:
            if char in char_set:
                char_set.remove(char)
                res += 2
            else:
                char_set.add(char)

        return res + 1 if char_set else res