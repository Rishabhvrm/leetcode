from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n, ten_power = 0, 0
        for i in range(len(digits) - 1, -1, -1):
            n += digits[i] * (10 ** ten_power)
            ten_power += 1
        
        n += 1

        res = []
        while n:
            res.append(n % 10)
            n //= 10

        return res[::-1]

    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        i = n - 1

        while i >= 0:
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            # it means digits[i] == 9
            digits[i] = 0
            i -= 1
        
        # it means that i < 0 and all values in digits are zeros now
        digits[0] = 1
        digits.append(0)

        return digits