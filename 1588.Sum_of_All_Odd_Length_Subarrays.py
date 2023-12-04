from typing import List
from typing import List
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        '''
        ## APPROACH-1: Sliding window
        ## TIME: O(n * n)
        ## SPACE: O(1)
        ws = 1 # window_size
        s = 0
        while ws <= len(arr):
            for i in range(len(arr) - ws + 1):
                s += sum(arr[i : i+ws])
            ws += 2
        return s
        '''

        ## APPROACH-2: brute forece
        ## TIME: O(n * n)
        ## SPACE: O(1)
        s = 0
        for i in range(len(arr)):
            for j in range(i, len(arr), 2):
                s += sum(arr[i : j+1])
        return s

obj = Solution()
arr = [1,4,2,5,3]
arr = [1,2]
arr = [10,11,12]
print(obj.sumOddLengthSubarrays(arr))