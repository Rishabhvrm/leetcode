from typing import List
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ## APPROACH-1: keep track of just sign, not the whole product
        ## TIME: O( n )

        '''
        sign = 1
        for n in nums:
            if n == 0: return 0
            elif n < 0: sign *= -1
        
        return sign
        '''

        ## APPROACH-2: keep count of -ve sign, if odd then -ve, if even then +ve
        ## TIME: O( n )
        neg_count = 0
        for n in nums:
            if n == 0: return 0
            elif n < 0: neg_count += 1
        
        return -1 if neg_count % 2 else 1