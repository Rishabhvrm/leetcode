from typing import List
from collections import deque
class Solution:
    '''
    min value for m and n 
    anything other than 0/1 ?
    what if all 1's?

    start multi-source BFS from all the 0s
    '''
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(mat), len(mat[0])
        visit = set()
        Q = deque()

        # Enque
        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 0:
                    visit.add((r,c))
                    Q.append((r,c))

        nghbrs = [(-1,0), (0,1), (1,0), (0,-1)]

        while Q:
            r, c = Q.popleft()
            d = mat[r][c]

            for dr, dc in nghbrs:
                nr, nc = r + dr, c + dc
                if ((nr, nc) not in visit and
                    nr in range(ROWS) and
                    nc in range(COLS)):
                    visit.add((nr, nc))
                    mat[nr][nc] = d + 1
                    Q.append((nr, nc))
        return mat