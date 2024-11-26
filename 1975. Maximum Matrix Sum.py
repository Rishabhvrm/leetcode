from typing import List


class Solution:
    '''
    observations:
    - if count of -ve #s is even => every # can be made +ve eventually
    - if count of -ve #s is odd => we can bring the count down to 1
    '''
    def maxMatrixSum(self, matrix: List[List[int]]) -> int: 
        ROWS, COLS = len(matrix), len(matrix[0])
        res_sum = 0
        abs_min_val = float('inf')
        negative_count = 0

        # for r in range(ROWS):
        #     for c in range(COLS):
        #         res_sum += abs(matrix[r][c])
        #         if matrix[r][c] < 0:
        #             negative_count += 1
        #         abs_min_val = min(abs_min_val, abs(matrix[r][c]))

        for rows in matrix:
            for num in rows:
                res_sum += abs(num)
                if num < 0:
                    negative_count += 1
                abs_min_val = min(abs_min_val, abs(num))

        return res_sum - (2 * abs_min_val) if negative_count % 2 else res_sum

        # 1   2  3
        # -1 10  3
        # 1   2  3