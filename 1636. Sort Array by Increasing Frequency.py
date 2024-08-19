from typing import List
from collections import Counter, defaultdict

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        num_freq = defaultdict(int)
        for n in nums:
            num_freq[n] += 1


        res = []
        for a, b in sorted(num_freq.items(), key=lambda x: (x[1], -x[0])):
            # for _ in range(b):
            #     res.append(a)
            res.extend([a] * b)

        return res

    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)

        def custom_sort(n):
            return (count[n], -n)

        nums.sort(key=custom_sort)

        return nums