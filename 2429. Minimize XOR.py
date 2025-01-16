
class Solution:
    '''
    001 101
    say x is 011 then 0 11 ^ 001 = 010
    say x is 101 then 101 ^ 001 = 100
    say x is 110 then 110 ^ 001 = 111
    '''

    '''
    How to set a bit at position i?
    - left shift 1 i times
    - OR with the org #

    How to unset a bit at position i?
    - left shift 1 i times
    - XOR with the org # (or NOT the above first and then AND with org #)

    How to check if a bit at position i is set?
    - left shift 1 i times
    - AND with org #
    - res should not be equal to 0 if ith bit is 1
    '''
    def minimizeXor(self, num1: int, num2: int) -> int:
        def is_set(num: int, bit_pos: int) -> bool:
            return num & (1 << bit_pos)

        def set_bit(num: int, bit_pos: int) -> int:
            return num | (1 << bit_pos)

        def unset_bit(num: int, bit_pos: int) -> int:
            return num ^ (1 << bit_pos)

        def count_set_bits(n: int) -> int:
            res = 0
            while n:
                res += 1 & n
                n = n >> 1
            return res

        x = num1
        curr_set_bits, req_set_bits = count_set_bits(num1), count_set_bits(num2)
        bit_pos = 0
        
        # add LSB
        while curr_set_bits < req_set_bits:
            if not is_set(x, bit_pos):
                x = set_bit(x, bit_pos)
                curr_set_bits += 1
            bit_pos += 1

        # remove LSB
        while curr_set_bits > req_set_bits:
            if is_set(x, bit_pos):
                x = unset_bit(x, bit_pos)
                curr_set_bits -= 1
            bit_pos += 1
            
        return x


    # def minimizeXor(self, num1: int, num2: int) -> int:
    #     def count_set_bits(n: int) -> int:
    #         res = 0
    #         while n:
    #             res += 1 & n
    #             n = n >> 1
    #         return res

    #     def is_set(num: int, bit_pos: int) -> bool:
    #         return num & (1 << bit_pos)

    #     x = num1
    #     curr_set_bits, req_set_bits = count_set_bits(num1), count_set_bits(num2)
        
    #     i = 0
    #     while curr_set_bits < req_set_bits:
    #         # if bit is set
    #         if not is_set(x, i):
    #             # x = x | (1 << i)        # set the bit
    #             curr_set_bits += 1
    #         i += 1
        
    #     i = 0
    #     while curr_set_bits > req_set_bits:
    #         if is_set(x, i):
    #             # x = x ^ (1 << i)        # unset the bit
    #             curr_set_bits -= 1
    #         i += 1
        
    #     return x