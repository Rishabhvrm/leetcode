from typing import List
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        ## APPROACH- brute force
        ## flatten the matrix and then fill the new matrix
        ## TIME: O( n * n ), traversing matrix
        ## SPACE: O( n * n), for new matrix
        m, n = len(mat), len(mat[0])        # get dimensions
        if m * n != r * c: return mat       # check if reshaping is possible


        # flatten org matrix
        flatten= []
        for row in mat:
            for num in row:
                flatten.append(num)

        # create reshaped matrix
        """
        reshape = [[0 for _ in range(c)] for _ in range(r)]
        p = 0
        for i in range(r):
            for j in range(c):
                reshape[i][j] = flatten[p]
                p += 1

        return reshape
        """
        # create reshaped matrix
        new_mat = []
        for i in range(0, len(flatten), c):
            new_mat.append(flatten[i : i+c])

        return new_mat

                

obj = Solution()
mat = [[1,2],[3,4]]
r = 1
c = 4
print(obj.matrixReshape(mat, r, c))