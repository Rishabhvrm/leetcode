class Solution:
    '''
    Idea: XOR a digit with 1 to flip it
    Time: O(log n)
    Space: O(1)
    '''
    def findComplement(self, num: int) -> int:
        bit_len = num.bit_length()

        mask = (1 << bit_len) - 1

        return num ^ mask
