class Solution:
    '''
    111000
    010101
    101010
    11110000
    10101010

    Approach: sliding window of size 2
    Time: O(n)
    Space: O(1)
    '''
    def minChanges(self, s: str) -> int:
        n = len(s)
        count = 0

        # if adjacent elements are both 1 or both 0
        # skip them
        # else increment the count (they must be different)
        # for i in range(0, n - 1, 2):
        #     if ((s[i] == "1" and s[i + 1] == "1") or
        #         (s[i] == "0" and s[i + 1] == "0")):
        #         continue
        #     else:
        #         count += 1
                
        # using this instead of above logic (that is correct too)
        # just check if adjacent elements are equal or not
        # if they're not then we have to change one of them in order to make 
        # the string beautiful
        for i in range(0, n - 1, 2):
            if s[i] != s[i + 1]:
                count += 1

        return count