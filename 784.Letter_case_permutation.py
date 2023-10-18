from typing import List
def letterCasePermutation(s: str) -> List[str]:

    ## TIME COMPLEXITY: O(2 ^ N), for both approaches
     
    ## APPROACH 1: Iterative

    # out = [""] # needs to be a empty string in it

    # for c in s:
    #     temp = []
    #     if c.isdigit():
    #         for o in out:
    #             temp.append(o+c)
    #     else:
    #         for o in out:
    #             temp.append(o+c.lower())
    #             temp.append(o+c.upper())   
    #     out = temp
    
    # return out

    ## APPROACH 2: RECURSIVE

    # output array
    permutations = []

    def backtrack(idx, ls):

        # base case
        if idx == len(s):
            return permutations.append(ls)

        # check if the ele is digit or alphabet
        ele = s[idx]
        if ele.isdigit():
            backtrack(idx + 1, ls + ele)
        # ele is alphabet
        else:
            backtrack(idx + 1, ls + ele.lower())
            backtrack(idx + 1, ls + ele.upper())

    backtrack(0, "")
    return permutations

