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

        for i in range(0, n - 1, 2):
            if ((s[i] == "1" and s[i + 1] == "1") or
                (s[i] == "0" and s[i + 1] == "0")):
                continue
            else:
                count += 1

        return count