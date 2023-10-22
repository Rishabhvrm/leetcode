from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        ## APPROACH: backtracking, decision tree, recursion
        ## TIME: O(2 ^ N)
        ## SPACE: O(N), for set.   * could be wrong

        def backtrack(start, curr_lst, total):
            # base cases
            if total == target:
                return res.append(curr_lst[:])
            
            if total > target or start >= len(candidates): return
            
            # Way 1
            # used = set()
            
            # Way 2
            previous = -1 # could by any value that can't exist in candidates
            
            for idx in range(start, len(candidates)):
                # 1st way to eliminate duplicates
                # if candidates[idx] not in used:
                #     used.add(candidates[idx])
                
                # 2nd way to eliminate duplicates
                if candidates[idx] != previous:   
                    previous = candidates[idx]   
                    
                    # include candidates[i]
                    curr_lst.append(candidates[idx])
                    backtrack(idx + 1, curr_lst, total + candidates[idx])
                    curr_lst.pop()

                    # NOT include candidates[i] - ??
                    # backtrack(idx + 1, curr_lst, total)

        res = []
        candidates.sort()
        backtrack(0, [], 0)
        return res

candidates = [10,1,2,7,6,1,5]
target = 8
s = Solution()
print(s.combinationSum2(candidates, target))