from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ## APPROACH-1: BRUTE FORCE
        ## TIME: O(M * N)
        ## SPACE: O(1)
        # ROWS, COLS = len(matrix) - 1, len(matrix[0]) - 1

        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if matrix[r][c] == target:
        #             return True
        # return False


        # APPROACH-2: BINARY SEARCH
        # TIME: O(LOG(M * N))
        # SPACE: O(1)

        ## APPROACH-2A: BINARY ON WHOLE MATRIX, DOESN'T WORK, MATRIX GETS HALF IN LENGTH AND BREADTH
        # ROWS, COLS = len(matrix) - 1, len(matrix[0]) - 1
        # left_row, left_col = 0, 0
        # right_row, right_col = ROWS, COLS
        
        # while left_row <= right_row and left_col <= right_col:
            
        #     mid_row = (left_row + right_row) // 2
        #     mid_col = (left_col + right_col) // 2

        #     if matrix[mid_row][mid_col] == target:
        #         return True
        #     # target lies in first half, update right values
        #     elif target < matrix[mid_row][mid_col]:
        #         right_row, right_col = mid_row, mid_col
        #     # target lies in second half, update left values
        #     elif target > matrix[mid_row][mid_col]:
        #         left_row, left_col = mid_row, mid_col
            
        # return False

        
        ## APPROACH-2B: BINARY ON ROWS AND COLUMNS SEPARATELY
        ROWS, COLS = len(matrix) - 1, len(matrix[0]) - 1
        
        # find target row
        top, bottom = 0, ROWS
        while top <= bottom:
            mid_row = (top + bottom)//2
            # if target > last value of mid row, target lies in bottom half
            if target > matrix[mid_row][COLS]:
                top = mid_row + 1
            # if target < first value of mid row, target lies in top half
            elif target < matrix[mid_row][0]:
                bottom = mid_row - 1            
            # target found
            else:
                break
            
        # if target not found
        if not (top <= bottom):
            return False
        

        # found the row
        # find the target
        row = (top + bottom) //2
        left, right = 0, COLS
        while (left <= right):
            mid_col = (left + right) // 2
            if target == matrix[row][mid_col]: return True
            elif target < matrix[row][mid_col]: right = mid_col - 1
            elif target > matrix[row][mid_col]: left = mid_col + 1
        return False

        
        

        ## ONLINE SOLUTION
        # ROWS, COLS = len(matrix), len(matrix[0])
        # left, right = 0, ROWS * COLS - 1

        # while left <= right:
        #     mid = (left + right) // 2
        #     mid_element = matrix[mid // COLS][mid % COLS] ???? HOW

        #     if mid_element == target:
        #         return True
        #     elif mid_element < target:
        #         left = mid + 1
        #     else:
        #         right = mid - 1

        # return False



matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 5

s = Solution()
print(s.searchMatrix(matrix, target))
