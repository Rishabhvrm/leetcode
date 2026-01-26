from typing import List
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        res = []
        min_diff = float('inf')

        arr.sort()

        for i in range(len(arr) - 1):
            min_diff = min(min_diff, (arr[i + 1] - arr[i]))
        
        for i in range(len(arr) - 1):
            if (arr[i + 1] - arr[i]) == min_diff:
                res.append([arr[i], arr[i + 1]])

        return res