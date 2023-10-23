from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def isPali(s, left, right):
            while left < right:
                if s[left] != s[right]: return False
                left += 1
                right += 1
            return True

        def backtrack(start, curr_part):
            if start == len(s):
                res.append(curr_part[:])
                return
            
            for idx in range(start, len(s)):
                if isPali(s, start, idx):
                    curr_part.append(s[start : idx + 1])
                    backtrack(idx + 1, curr_part)
                    curr_part.pop()

        res = []
        backtrack(0, [])
        return res

s = Solution()
print(s.partition("aab"))