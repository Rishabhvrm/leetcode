from typing import List
class Solution:
    '''
       i
    LeetcodeHelpsMeLearn

res = Le e
    approach: Brute force/simulate
    2 pointers, one to traverse the s and other spaces
    if spaces[b] == idx in s, append a space to res
    Time: O(n + m), n: len of s and m: len of spaces
    Space: O(n), output res
    '''
    '''
    abcd
    0,1,2,3
    " a b c d"
    '''
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        a, b = 0, 0

        while a < len(s):
            if b < len(spaces) and a == spaces[b]:
                res.append(" ")
                b += 1
            res.append(s[a])
            a += 1

        return "".join(res)
