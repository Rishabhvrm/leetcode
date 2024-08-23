from math import log

class Solution:

    '''
    Approach: XOR each digit with 1 to flip it. One-by-one
    Time: O(log n)
    Space: O(1)
    '''
    def findComplement(self, num: int) -> int:
        bit_len = int(log(num, 2)) + 1
        
        for i in range(bit_len):
            num ^= 1 << i
        return num


    '''
    Idea: XOR a digit with 1 to flip it
    Time: O(log n)
    Space: O(1)
    '''
    def findComplement(self, num: int) -> int:
        bit_len = num.bit_length()

        mask = (1 << bit_len) - 1

        return num ^ mask

    '''
    Approach: XOR each digit with 1 to flip it. One-by-one
    Time: O(log n)
    Space: O(1)
    '''
    def findComplement(self, num: int) -> int:
        i = 0
        comp = 0

        while num:
            if(num & 1 == 0):     # flip
                comp |= 1 << i

            num >>= 1
            i += 1

        return comp