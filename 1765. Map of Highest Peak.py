from typing import List
from collections import deque
class Solution:
    '''
    isWater:
    0 1
    0 0

    Height:
    1 0
    2 1

    isWater:
    0 0 1
    1 0 0
    0 0 0

    Height:
    - - 0
    0 - -
    - - -

    ==> 
    
    1 1 0
    0 1 1
    1 2 2

    min distance of nearest 0 from each cell in the height matrix
    Multisource BFS
    '''
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(isWater), len(isWater[0])
        Q = deque() # (r,c)
        visit = set()      # can use a new grid filled with -1

        # enque water cells
        for r in range(ROWS):
            for c in range(COLS):
                if isWater[r][c] == 1:
                    Q.append((r,c))
                    visit.add((r,c))
                    isWater[r][c] = 0

        nghbrs = [(0,1), (0,-1), (1,0), (-1,0)]

        while Q:
            row, col = Q.popleft()
            h = isWater[row][col]
            
            for dr, dc in nghbrs:
                new_row, new_col = row + dr, col + dc
                if ((new_row, new_col) not in visit and
                    new_row in range(ROWS) and new_col in range(COLS)
                    ):
                    Q.append((new_row, new_col))
                    isWater[new_row][new_col] = h + 1
                    visit.add((new_row, new_col))

        return isWater

