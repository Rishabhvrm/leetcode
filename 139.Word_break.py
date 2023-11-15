from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ## APPROACH: DP
        ## TIME: O (n * n)
        n = len(s)
        word_set = set(wordDict)        # for faster lookup
        
        # consider an empty string as a valid segmentation
        dp = [False] * (n + 1)
        dp[0] = True

        for right in range(1, n + 1):
            for left in range(right):
                substring = s[left : right]
                # dp[left] = True means we were able to find a word
                # in wD that ended at idx = left, it means till idx = left in s, 
                # everything is covered (substring[start:left] occurs in wD)
                if dp[left] and substring in word_set:
                    dp[right] = True
                    break
        return dp[n]
    

        ## APPROACH-2: BRUTE FORCE
        ## TIME: O( n * n * n )
        '''
        def wordBreak2(self, s, wordDict):
            n = len(s)
            i = 0
            while i < n: 
                for j in range(i, n):
                    substring = s[i : j + 1]
                    if substring in wordDict:
                        if j == n - 1: return True
                        i = j + 1
                i += 1
            return False
        '''
    
obj = Solution()
s1, wordDict1 = "leetcode", ["leet","code"]
s2, wordDict2 = "applepenapple", ["apple","pen"]
s3, wordDict3 = "catsandog", ["cats","dog","sand","and","cat"]
s4, wordDict4 = "aaaaaaa", ["aaaa","aaa"] # this fails 

print(obj.wordBreak1(s1, wordDict1))
# print(obj.wordBreak1(s2, wordDict2))
# print(obj.wordBreak1(s3, wordDict3))
# print(obj.wordBreak1(s4, wordDict4))

# print(obj.wordBreak2(s1, wordDict1))
# print(obj.wordBreak2(s2, wordDict2))
# print(obj.wordBreak2(s3, wordDict3))
# print(obj.wordBreak2(s4, wordDict4))