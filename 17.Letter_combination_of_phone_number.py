from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        ## APPROACH: BACTRACKING
        ## TIME: O(4 ^ n)
        ## SPACE: O(n)
        def backtrack(idx, curr_str):
            # base case
            if len(curr_str) == len(digits):
                res.append("".join(curr_str[:]))
                return

            for char in map[digits[idx]]:
                curr_str.append(char)
                backtrack(idx + 1, curr_str)
                curr_str.pop()
        
        map = {
            "2": ["a","b","c"],
            "3": ["d","e","f"],
            "4": ["g","h","i"],
            "5": ["j","k","l"],
            "6": ["m","n","o"],
            "7": ["p","q","r","s"],
            "8": ["t","u","v"],
            "9": ["w","x","y","z"]
        }

        res = []
        if digits:
            backtrack(0, [])
        return res


s = Solution()
print(s.letterCombinations("23"))