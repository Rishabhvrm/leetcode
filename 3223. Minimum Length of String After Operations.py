from collections import defaultdict
class Solution:
    '''
    
    SxxSxSxSxS
    xxSxxS
    xSxS

    SS => SS
    SSSS => SS
    SS => 

    SSS =>
    SSS 

    if n is odd (> 3) then you can bring it down to 1
    if n is even (> 2) then you can bring it down to 2

    abaacbcbb
    
    a: 3    => 1
    b: 4    => 2
    c: 2    => 2
    
    '''
    '''
    Approach: using set, 
    realise that every even occurance can be reduced to 2
    and; every odd occurance can be reduced to 1
    Time: O(n), n: len of s
    Space: O(n), dict, if every char is unique
    '''
    def minimumLength(self, s: str) -> int:
        char_occ = defaultdict(int)
        res = 0

        # make counter
        for c in s:
            char_occ[c] += 1
    
        # add 1 if odd else add 2
        for k, v in char_occ.items():
            res += 1 if v % 2 else 2

        return res