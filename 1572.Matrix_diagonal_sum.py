from typing import List
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        '''
        ## APPROACH-1: brute force, 
        ## primary diagonal, pick elements where i == j, diff is constant
        ## secondary diagonal, sum is constant
        ## use a set to eliminate duplicates
        ## TIME: O( n * n )
        ## SPACE: O( n )
        ROWS, COLS = len(mat), len(mat[0])
        s = 0
        visited = set()

        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) not in visited and ((i - j) == 0 or (i + j) == COLS - 1):
                    visited.add((i, j))
                    s += mat[i][j]
        
        return s
        '''

        ## APPROACH-2: single loop
        ## TIME: O( n )
        ## SPACE: O( 1 )
        n = len(mat)
        s = 0

        for i in range(n):
            s += mat[i][i]              # primary diagonal
            s += mat[n - 1 - i][i]      # secondary diagonal

        # if n is odd, remove duplicate
        if n % 2:
            s -= mat[n // 2][n // 2]
        
        return s

    
obj = Solution()
mat = [[1,2,3], [4,5,6], [7,8,9]]
print(obj.diagonalSum(mat))