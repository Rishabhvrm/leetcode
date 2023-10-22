from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []

        def backtrack(idx, curr_lst, total):
            # base cases
            if total == target:
                res.append(curr_lst[:])
                return
            if total > target or idx >= len(candidates):
                return

            # include candidate
            curr_lst.append(candidates[idx])
            backtrack(idx, curr_lst, total + candidates[idx])
            curr_lst.pop()

            # NOT include the candidate
            backtrack(idx + 1, curr_lst, total)


        backtrack(0,[],0)
        return res