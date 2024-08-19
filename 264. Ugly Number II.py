from typing import List

class Solution:
    '''
    Brute Force: count all ugly numbers till n
    TLE 409/596
    '''
    # def nthUglyNumber(self, n: int) -> int:
    #     def _is_ugly(num):
    #         if num < 1: return False

    #         for p in [2,3,5]:
    #             while num % p == 0:
    #                 num /= p

    #         return num == 1

    #     res = []
    #     count = 0
    #     i = 0
    #     while count < n:
    #         if _is_ugly(i):
    #             res = i
    #             count += 1
    #         i += 1

    #     return res
    
    # def nthUglyNumber(self, n):
    #     primes = [2,3,5]
    #     uglyHeap = [1]
    #     visited = set()
    #     visited.add(1)
    #     for _ in range(n):
    #         curr = heappop(uglyHeap)
    #         for prime in primes:
    #             new_ugly = curr * prime
    #             if new_ugly not in visited:
    #                 heappush(uglyHeap, new_ugly)
    #                 visited.add(new_ugly)
    #     return curr

    '''
    DP
    '''
    def nthUglyNumber(self, n: int) -> int:
        nums = [1]
        i2, i3, i5 = 0, 0, 0

        for i in range(1, n):
            next_num = min(
                nums[i2] * 2, nums[i3] * 3, nums[i5] * 5
            )
            nums.append(next_num)

            if next_num == nums[i2] * 2:
                i2 += 1
            if next_num == nums[i3] * 3:
                i3 += 1
            if next_num == nums[i5] * 5:
                i5 += 1

        print(nums)
        return nums[-1]