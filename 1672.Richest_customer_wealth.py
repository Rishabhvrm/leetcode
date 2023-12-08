from typing import List
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ## APPROACH: brute force, calculate sum for every row and update max_wealth
        ## TIME: O(n * n), for loop and sum()
        ## SPACE: O(1)

        max_wealth = 0

        for acc in accounts:
            max_wealth = max(max_wealth, sum(acc))

        return max_wealth

        # return max(sum(acc) for acc in accounts)