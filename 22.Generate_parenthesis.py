from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ## APPROACH: recursion, decision tree, rules to follow for it
        ## TIME: O(2 ^ N)
        ## Space: res array, O(2 ^ N) and recursion stack memory, could be right

        def backtrack(open_count, close_count, curr_lst):
            # base case
            if len(curr_lst) == limit:
            # if open_count == close_count == n:
                res.append("".join(curr_lst))
                return

            if open_count < n:
                # append open parenthesis
                curr_lst.append("(")
                # shouldn't do this, we don't want o_c to change in current function
                # open_count += 1 
                backtrack(open_count + 1, close_count, curr_lst)
                curr_lst.pop()

            if close_count < open_count:
                # append close parenthesis
                curr_lst.append(")")
                # shouldn't do this, we don't want o_c to change in current function
                # close_count += 1
                backtrack(open_count, close_count + 1, curr_lst)
                curr_lst.pop()

        limit = n * 2
        res = []
        backtrack(0,0,[])
        return res
