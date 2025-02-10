from typing import List


class Solution:
    '''
     l
    b******
          r

    li
    li5i56
        *
        *
    baaa123
    baa
    '''
    '''
    brute force
    '''
    def clearDigits(self, s: str) -> str:
        res = list(s)
        a, b = 0, 0
        
        while b < len(s):
            if res[b].isdigit():
                res[b] = ""                                                 # mark digit at b
                a = b - 1
                first_char = True
                while a >= 0 and first_char:                                # find & mark char left to digit
                    first_char = False if res[a] != "" else True
                    res[a] = ""
                    a -= 1
            b += 1
        
        return "".join(res)

    '''
    using stack
    Time: O(n)
    Space: O(n)
    '''
    def clearDigits(self, s: str) -> str:
        stack = []
        
        for c in s:
            if c.isdigit():
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        
        return "".join(stack)