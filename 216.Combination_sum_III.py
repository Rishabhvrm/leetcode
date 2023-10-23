from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        

        ## APPROACH: decision tree
        ## T(N): O(N ^ K)
        ## Space: no extra space except res[] + recursion stack memory
        
        def backtrack(start, total, curr_lst):
            l = len(curr_lst)
            
            # base case
            if l > k or total > n: 
                return
            if total == n and l == k: 
                res.append(curr_lst[:])
                return
            
            for idx in range(start, len(candidates)):
                curr_lst.append(candidates[idx])
                backtrack(idx + 1, total + candidates[idx], curr_lst)
                curr_lst.pop() # backtrack

        res = []
        candidates = [1,2,3,4,5,6,7,8,9]
        backtrack(0, 0, [])
        return res