'''
use built in functions like bin(n)[2:].count('1') or collections.Counter

or use bit-manipulation
AND with 1 to check if LSB is 1, if yes increase the count and then move onto next bit by right shifting the number (using n  >> 1)
'''

class Solution:
    def hammingWeight(self, n: int) -> int:
        
        ## using in-built function
        '''
        counter = collections.Counter(bin(n)[2:])
        return counter.get("1", 0)
        '''
        
        '''
        return bin(n)[2:].count('1')
        '''

        ## using bit-manipulation
        count = 0

        while n:
            # AND with 1 to check if LSB is 1
            if n & 1: count += 1
            # right shift n to check next bit
            n = n >> 1

        return count