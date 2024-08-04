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
        
    '''
    Approach: top-down recursive memoization
    Time and Space: O(m * n)
    '''
    # def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    #     memo = {}           # (a,b) = max_len for this combination of a,b
        
    #     def solve(i,j):
    #         if i >= len(text1) or j >= len(text2):
    #             return 0

    #         if (i,j) in memo:
    #             return memo[(i,j)]

    #         if text1[i] == text2[j]:
    #             memo[(i,j)] =  1 + solve(i + 1, j + 1)
    #         else:
    #             memo[(i,j)] = max(solve(i + 1, j), solve(i, j + 1))
    #         return memo[(i,j)]

        # return solve(0, 0)

    '''
    State definition:
    LCS btw s1 (till idx i) and s2 (till idx j)

    need 0th col and 0th row bcz we take max(i-1, j-1)

    Approach: Bottom-Up
    Time and Space: O(m * n)
    '''
    # def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    #     ROWS, COLS = len(text1), len(text2)

    #     grid = [[0 for _ in range(COLS + 1)] for _ in range(ROWS + 1)]
        
    #     for i in range(1, ROWS + 1):
    #         for j in range(1, COLS + 1):
    #             if text1[i - 1] == text2[j - 1]:
    #                 grid[i][j] = 1 + grid[i - 1][j - 1]
    #             else:
    #                 grid[i][j] = max(grid[i][j - 1], grid[i - 1][j])
        
    #     return grid[ROWS][COLS]
        
    '''
    Approach: Same as above, just going right to left
    Time and Space: O(m * n)
    '''
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1) - 1, len(text2) - 1
        memo = {}       # LCS for given (i,j)

        def solve(i, j):
            if i < 0 or j < 0:
                return 0

            if (i, j) in memo:
                return memo[(i,j)]

            if text1[i] == text2[j]:
                memo[(i,j)] = 1 + solve(i - 1, j - 1)
            else:
                memo[(i,j)] = max(solve(i - 1, j), solve(i, j - 1))
            return memo[(i,j)]

        return solve(m, n)