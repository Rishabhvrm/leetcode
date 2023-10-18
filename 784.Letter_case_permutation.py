from typing import List
def letterCasePermutation(s: str) -> List[str]:

    # APPROACH1- Iterative

    out = [""] # needs to be a empty string in it

    for c in s:
        temp = []
        if c.isdigit():
            for o in out:
                temp.append(o+c)
        else:
            for o in out:
                temp.append(o+c.lower())
                temp.append(o+c.upper())   
        out = temp
    
    return out