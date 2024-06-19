class Solution:
    '''
         i
    aababcabc
           j

          *  #  #  
    0  1  2  3  4    
    a, b, c, d, e

    {abc, bca, }
    Brute force
    '''
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3:
            return 0

        ans = 0
        for i in range(len(s) - 2):
            uniques = set()
            uniques.add(s[i])

            for j in range(i + 1, i + 3):
                if s[j] not in uniques:
                    uniques.add(s[j])
                else:
                    break

                if j - i == 2:
                    ans += 1

        return ans
    
    '''
    Sliding window
    
        *
    xyzzaz
    012345

    '''
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3:
            return 0

        ans = 0
        l = 0
        for r in range(2, len(s)):
            a, b = s[r - 2], s[r - 1]
            if (s[r] != a and s[r] != b) and (a != b):
                ans += 1
        return ans
            


