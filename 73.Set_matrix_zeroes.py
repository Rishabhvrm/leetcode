class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        ## APPROACH 1: 
        ## find out i and j values for all the zeros in matrix, and store them
        ## for rows: make the whole row 0
        ## for columns: make the same place in every internal array as 0
        
        ## T(N): O(N * N * N)
        ## Space: O(N)

        # m rows and n columns
        # m, n = len(matrix), len(matrix[0])
        # col_0, row_0 = [], []
        # arr = []
        
        # traverse matrix to find out i and j values for 0 elements
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == 0:
        #             col_0.append(i)
        #             row_0.append(j)

        # # make all column values in matrix as 0 for every c in col_0
        # for c in col_0:
        #     for i in range(m):
        #         for j in range(n):
        #             if i == c:
        #                 matrix[i][j] = 0

        # # make all row values in matrix as 0 for every r in row_0
        # for r in row_0:
        #     for i in range(m):
        #         for j in range(n):
        #             if j == r:
        #                 matrix[i][j] = 0


        ## APPROACH 2: 
        ## approach is same as above but coding it differently
        
        ## T(N): O(N * N)
        ## Space: O(N)

        # traverse matrix to find out i and j values for 0 elements
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == 0:
        #             col_0.append(i)
        #             row_0.append(j)
        #             arr.append([i,j])

        # for r, c in arr:                # m rows and n columns
        #     for i in range(m):          # update columns
        #         matrix[i][c] = 0
        #     for j in range(n):          # update rows
        #         matrix[r][j] = 0


        ## APPROACH 3: Neetcode solution 
        ## taking the extra arrays (col_0, row_0 = [], []) 
        ## inside the matrix, using constant space      
        ## T(N): O(N * N)
        ## Space: O(1)

        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False

        # determine which col/row needs to be zero
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else: rowZero = True

        # 0 out the matrix except 1st row and 1st col
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # 0 out the 1st col (if required)
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        # 0 out the 1st row(if required)
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0

matrix = [[1,1,1],[1,0,1],[1,1,1]]
matrix2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# setZeroes(matrix2)
    
l = [[1,2],[3,4],[5,6]]
for i, j in l:
    print(i,j)