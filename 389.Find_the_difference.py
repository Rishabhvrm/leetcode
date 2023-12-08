class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ## APPROACH-1: using set
        # can't use set on s = "a", t = "aa

        '''
        ## APPROACH-2: check count of each char in both strings
        ## TIME: O(n * n), for loop and count()
        for c in t: 
            if s.count(c) != t.count(c): return c
        '''

        '''
        ## APPROACH-3: using set bit-manipulation; ord() and chr()
        res = 0

        for c in s:
            res ^= ord(c)

        for c in t:
            res ^= ord(c)

        return chr(res)
        '''
            
        ## APPROACH-4: using ASCII Sum ord()
        sum_s = sum(ord(char) for char in s)
        sum_t = sum(ord(char) for char in t)

        diff = sum_t - sum_s        # find ASCII difference
        return chr(diff)            # convert ASCII difference to char


obj = Solution()
s = "abcd"
t = "abcde"
print(obj.findTheDifference(s,t))