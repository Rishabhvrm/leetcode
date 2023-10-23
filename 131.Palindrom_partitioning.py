from typing import List
class Solution:

    ## APPROACH: decision tree, check palindrome, substring
    ## TIME: O(2 ^ N), each char can be part of palindrome or not => 2 choices
    ## SPACE: O(N), recursion stack = depth of tree, curr_part => upto N

    def is_palindrome(self, s):
        return s == s[::-1]

    def partition(self, s: str) -> List[List[str]]:

        def backtrack(start, curr_part):

            # base case
            if start == len(s):
                res.append(curr_part[:])
                return

            for end in range (start, len(s)):
                substring = s[start : end + 1]

                # only make tree further if substring is palindrome
                if self.is_palindrome(substring):
                    curr_part.append(substring)
                    backtrack(end + 1, curr_part)
                    curr_part.pop()

        res = []
        backtrack(0,[])
        return res

s = Solution()
print(s.partition("aab"))