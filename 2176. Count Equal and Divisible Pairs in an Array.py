from typing import List
from collections import defaultdict
class Solution:
    '''
    brute force: O(n * n)
    '''
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    count += 1
        
        return count

    '''
    using map:
    1, 1, 1, 1, 1
    1: [0, 1, 2, 3, 4]
    better but still n ** 2
    '''
    def countPairs(self, nums: List[int], k: int) -> int:
        num_idx = defaultdict(list)
        count = 0

        for i, n in enumerate(nums):
            num_idx[n].append(i)

        for indices in num_idx.values():
            for i in range(len(indices)):
                for j in range(i + 1, len(indices)):
                    if (indices[i] * indices[j]) % k == 0:
                        count += 1

        return count