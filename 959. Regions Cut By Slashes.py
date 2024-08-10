from typing import List
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        rows, cols = len(grid), len(grid[0])
        ROWS, COLS = 3 * rows, 3 * cols
        GRID = [[0] * COLS for _ in range(ROWS)]

        # make GRID
        for r in range(rows):
            for c in range(cols):
                R, C = r * 3, c * 3
                if grid[r][c] == "/":
                    GRID[R][C + 2]     = 1
                    GRID[R + 1][C + 1] = 1
                    GRID[R + 2][C]     = 1
                elif grid[r][c] == "\\":
                    GRID[R][C]         = 1
                    GRID[R + 1][C + 1] = 1
                    GRID[R + 2][C + 2] = 1


        def _dfs(r, c):
            if (
                not (0 <= r < ROWS) or
                not (0 <= c < COLS) or
                (r, c) in visited or
                GRID[r][c] != 0
            ):
                return
            
            visited.add((r, c))

            directions = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            for nr, nc in directions:
                _dfs(nr, nc)


        # no. of island
        visited = set()
        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and GRID[r][c] == 0:
                    _dfs(r,c)        # or regions
                    islands += 1
        
        return islands