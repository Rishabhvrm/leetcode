from itertools import pairwise
class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        for i in range(1, len(s)):
            res += abs(ord(s[i - 1]) - ord(s[i]))

        return res

    # using pairwise
    def scoreOfString(self, s: str) -> int:
        return sum(abs(ord(a) - ord(b)) for a, b in pairwise(s))