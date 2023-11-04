from typing import List
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        ## APPROACH: Bottom-Up, tabulation, iteration
        ## TIME: O(n * m)
        ## SPACE: O(n * m)

        # The first line creates a matrix with rows that are references to the same list, 
        # while the second line creates a proper 2D matrix with distinct lists for each row
        # dp = [[0] * (len(text2) + 1)] * (len(text1) + 1)
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        for i in range(len(text1) -1, -1, -1):
            for j in range(len(text2) -1, -1, -1):
                # if chars match, add one move diagonally up
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                # if chars don't match, pick max(bottom, right)
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]
        