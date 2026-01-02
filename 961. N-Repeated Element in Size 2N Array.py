from random import sample
from typing import List
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen = set()
        for n in nums:
            if n in seen:
                return n
            seen.add(n)
            
    def repeatedNTimes(self, nums: List[int]) -> int:
        # Randomization (Average Time: $O(1)$, Space: $O(1)$)Since half of the elements are the target, if you pick two indices at random, there is a very high probability (25%) they will both be the repeated element.
        while True:
            i, j = sample(range(len(nums)), 2)
            if nums[i] == nums[j]:
                return nums[i]