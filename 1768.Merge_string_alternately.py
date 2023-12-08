class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ## APPROACH: 2 pointers, brute force
        ## TIME: O(n)
        ## SPACE: O(n), output list/string

        i, j = 0, 0
        res = []

        # append letters alternatively
        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1
        
        # add any remaining letters
        if i < len(word1):
            res.append(word1[i:])

        if j < len(word2):
            res.append(word2[j:])
        
        return "".join(res)
    
        '''
        # shorter code
        for i in range(n):
            st += word1[i] + word2[i]
        return st + word1[n:] + word2[n:]
        '''

obj = Solution()
# word1 = "abc"
# word2 = "pqr"
word1 = "ab"
word2 = "pqrs"
print(obj.mergeAlternately(word1, word2))