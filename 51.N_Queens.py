from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def backtrack(row):
            # base case
            if row == n: 
                # output format, whole board is one row
                copy = ["".join(r) for r in board]
                res.append(copy)
                return
            
            for col in range(n):
                # skip the positions where a queen kills any other queen
                if col in COLS or (row + col) in pos_diag or (row - col) in neg_diag:
                    continue            # skip this position

                COLS.add(col)
                pos_diag.add(row + col)
                neg_diag.add(row - col)
                board[row][col] = "Q"

                backtrack(row + 1)

                # undo <=> backtrack from one branch to other
                COLS.remove(col)
                pos_diag.remove(row + col)
                neg_diag.remove(row - col)
                board[row][col] = "."

        # keep track of cells where a queen can kill another queen
        #     (r + c)   (r - c)
        COLS, pos_diag, neg_diag = set(), set(), set()
        res = []
        board = [["."] * n for i in range(n)]

        # start from first row
        backtrack(0)
        return res


obj = Solution()
print(obj.solveNQueens(4))