from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ## APPROACH: Backtracking/recursion
        ## T(N): O(n * n!)
        ## Space: O(n!)

        def backtrack(first):
            # base cases
            if first == n:
                return res.append(nums[:])
            
            for idx in range(first, n):
                # swap
                nums[first], nums[idx] = nums[idx], nums[first]
                
                # backtrack
                backtrack(first + 1)

                # undo
                nums[first], nums[idx] = nums[idx], nums[first]
        
        res = []
        n = len(nums)
        backtrack(0)
        return res
    
nums = [1,2,3]
sol = Solution()
print(sol.permute(nums))
