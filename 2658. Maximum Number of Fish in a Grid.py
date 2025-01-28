from typing import List
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        # returns max fish collected starting from r,c
        def dfs(r,c) -> int:
            if (
                (r,c) in visited or
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                grid[r][c] == 0
            ):
                return 0
            
            visited.add((r,c))
            neighbors = [(0, 1), (0, -1), (-1, 0), (1, 0)]
            curr_sum = grid[r][c]

            for dr, dc in neighbors:
                nr, nc = r + dr, c + dc
                curr_sum += dfs(nr, nc)

            return curr_sum

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        res = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    res = max(res, dfs(r,c))
        return res
