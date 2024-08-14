from typing import List

'''
I:
    +ve, and >= 1
    repeat? => yes
    target >= 1

O:
    [1], t = 4 => Output = [  ] if no solution exist
    [1,1], t = 2 => output = [ [1,1] ]

APPROACHES:
    Give TLE, repeated work
    1: 2 choices at every level,
            stop when sum goes beyond or find ans or idx goes beyond len
            remove duplicates by using a set while adding to final res
    
    Good backtracking approach, skips duplicates
    2: left skewed tree where from any point there are only branches forward
            skip duplicate branches, need to be sorted so that adjacent elements can be compared
            use a for loop and compare current and prev branch
'''
'''
approach-1: complete binary tree with 2 choices at every node
TLE at 172/176
'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        ## APPROACH: backtracking, decision tree, recursion
        ## TIME: O(2 ^ N)
        ## SPACE: O(N), for set.   * could be wrong
        ##        O(1), if set not used
        ##        in both cases recursion stack memory is used


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