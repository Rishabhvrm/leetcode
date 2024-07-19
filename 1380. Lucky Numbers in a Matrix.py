from math import inf
from typing import List


class Solution:
    '''

    [3,  7, 8],
    [9, 11, 13],
    [15, 16,17]

    3 9 15
    15 16 17
    '''
    '''
    APPROACH-1: find all min_vals for rows and min_vals for cols,
    only 1 element would be common, return that
    Time: O(N * M)
    Space: O(N + M)
    '''
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        mins, maxs = set(), set()
        ROWS, COLS = len(matrix), len(matrix[0])

        for r in range(ROWS):
            min_ele_row = float('inf')
            for c in range(COLS):
                min_ele_row = min(min_ele_row, matrix[r][c])
            mins.add(min_ele_row)

        for c in range(COLS):
            max_ele_row = float('-inf')
            for r in range(ROWS):
                max_ele_row = max(max_ele_row, matrix[r][c])
            maxs.add(max_ele_row)

        return list(mins.intersection(maxs))

    '''
    failed for checking only row_min_max

    [3,6],
    [7,1],
    [5,2],
    [4,8]

    3 1 2 4
    7 8
    nothing common

    APPROACH-2: 
    find all min_vals for rows, take max out of those vals
    find all max_vals for cols, take min out of those vals
    if both vals are same, then that is the answer
    Time: O(N * M)
    Space: O(1)
    '''
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:

        ROWS, COLS = len(matrix), len(matrix[0])
        row_min_max = -inf
        col_max_min = inf

        for r in range(ROWS):
            row_min = min(matrix[r])
            row_min_max = max(row_min_max, row_min)

        for c in range(COLS):
            col_max = max(matrix[r][c] for r in range(ROWS))
            col_max_min = min(col_max_min, col_max)

        return [row_min_max] if row_min_max == col_max_min else []