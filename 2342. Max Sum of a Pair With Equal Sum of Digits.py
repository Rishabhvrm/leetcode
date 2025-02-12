from typing import List
class Solution:
    '''

    9. 7. 9. 4. 7 9
    18,43,36,13,7,81
    '''
    def maximumSum(self, nums: List[int]) -> int:

        def sum_of_digits(num):
            digit_sum = 0
            while num:
                digit_sum += num % 10
                num //= 10
            return digit_sum

        sum_vals = defaultdict(list)
        res = 0

        for n in nums:
            sum_vals[sum_of_digits(n)].append(n)

        for k,v in sum_vals.items():
            v.sort(reverse=True)

        for k,v in sum_vals.items():
            res = max(res, v[0] + v[1] if len(v) >= 2 else 0)

        return res if res != 0 else -1