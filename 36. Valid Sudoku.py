from collections import defaultdict
from typing import List


class Solution:
    '''
    APPROACH: BRUTE FORCE,
    TIME: O(N ^ 2)
    SPACE: O(N), for sets
    '''
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check if a row contains duplicate
        # check if a col contains duplicate
        # check if a box contains duplicate

        # if any row contains duplicate then return false
        def check_row():
            for row in board:
                row_set = set()
                for ele in row:
                    if ele == ".": continue
                    if ele not in row_set: row_set.add(ele)
                    else: return False
            return True
            
        # if any col contains duplicate then return false
        def check_col():
            for j in range(COLS):
                col_set = set()
                for i in range(ROWS):
                    if board[i][j] == ".": continue
                    if board[i][j] not in col_set: col_set.add(board[i][j])
                    else: return False
            return True

        # if any box contains duplicate then return false
        def check_box():
            for row_val in range(0, 9, 3):
                for col_val in range(0, 9, 3):
                    box_set = set()
                    for i in range(row_val, row_val + 3):
                        for j in range(col_val, col_val + 3):
                            if board[i][j] == ".": continue
                            if board[i][j] not in box_set: box_set.add(board[i][j])
                            else: return False
            return True

        ROWS, COLS = len(board), len(board[0])
        return (check_row() and check_col() and check_box())

    '''
    APPROACH: same logic as above but diff code
    TIME: O(N ^ 2)
    SPACE: O(N), for sets
    '''
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        cols = defaultdict(set)              # { col_number: {values in this column} } => { 3: {3,5,7,1} }
        rows = defaultdict(set)              # { row_number: {values in this row} } => { 3: {3,5,7,1} }
        boxes = defaultdict(set)             # { (box_row_number, box_col_number): {values in this box} } => { (1,1): {3,5,7,1} }

        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if board[r][c] != ".":
        #             #check failing condition
        #             if board[r][c] in rows[r] or /
        #                 board[r][c] in cols[c] or /
        #                 board[r][c] in boxes[(row//2, col//2)]:


        # if this element (i.e. board[i][j]) occurs in this row_number (i.e. row[i]) or it occurs in this col_number (i.e. col[j])

board = [[".",".",".",".","5",".",".","1","."],
         [".","4",".","3",".",".",".",".","."],
         [".",".",".",".",".","3",".",".","1"],
         ["8",".",".",".",".",".",".","2","."],
         [".",".","2",".","7",".",".",".","."],
         [".","1","5",".",".",".",".",".","."],
         [".",".",".",".",".","2",".",".","."],
         [".","2",".","9",".",".",".",".","."],
         [".",".","4",".",".",".",".",".","."]]
# board = [["5","3",".",".","7",".",".",".","."], ["5","3",".",".","7",".",".",".","."]]
print(Solution().isValidSudoku(board))