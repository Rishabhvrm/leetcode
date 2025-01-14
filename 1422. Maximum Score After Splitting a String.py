from typing import List
class Solution:
    '''
    10
    1100
    1111
    0000

    keep counting 0s until you reach n - 1
    if first ele is 1 or encounter 1 anywhere : start counting 1s until end

    '''
    # def maxScore(self, s: str) -> int:
        

    '''
    brute force
    '''
    def maxScore(self, s: str) -> int:
        res, curr_res = 0, 0
        s = list(s)

        # checking every split point
        for i in range(1, len(s)):
            zeros, ones = 0, 0

            for a in range(0, i):
                if s[a] == "0":
                    zeros += 1

            for b in range(i, len(s)):
                if s[b] == "1":
                    ones += 1

            curr_res = zeros + ones

            res = max(res, curr_res)
            
        return res
    
    '''
    one pass
    '''
    def maxScore(self, s: str) -> int:
        zeros, ones = 0, 0
        for c in s:
            if c == "1":
                ones += 1

        res = 0
        for i in range(len(s) - 1):
            c = s[i]
            if c == "0":
                zeros += 1
            else:
                ones -= 1
            
            res = max(res, zeros + ones)

        return res


