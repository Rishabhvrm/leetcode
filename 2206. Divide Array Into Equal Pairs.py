from typing import List
from collections import defaultdict
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        num_freq = defaultdict(int)

        for n in nums:
            num_freq[n] += 1
        
        for k, v in num_freq.items():
            if v % 2:
                return False

        return True