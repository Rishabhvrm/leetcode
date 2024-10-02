from typing import List
from collections import defaultdict
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        rem_count = defaultdict(int)

        for n in arr:
            rem_count[(n % k + k) % k] += 1
        
        if rem_count[0] % 2:
            return False
            
        for r in range(1, (k // 2) + 1):
            
            # if r == k - r:  # Special case for the middle remainder when k is even
            #     if rem_count[r] % 2 != 0:
            #         return False

            if rem_count[r] != rem_count[k - r]:
                return False

        return True