from typing import List
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        ## APPROACH: sort and traverse while checking difference
        ## TIME: O (n * logn)
        arr.sort()
        diff = abs(arr[1] - arr[0])

        for i in range(1, len(arr) - 1):
            if abs(arr[i + 1] - arr[i]) != diff:
                return False

        return True
    
obj = Solution()
arr = [1,5,3,7]
print(obj.canMakeArithmeticProgression(arr))