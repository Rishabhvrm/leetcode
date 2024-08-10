from typing import List
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def _check_boundary(r, c):
            nonlocal count
            if (
                not (0 <= r < rows) or
                not (0 <= c < cols) or
                grid[r][c] == 0
            ):
                count += 1

        def _dfs(r, c):
            if (
                not (0 <= r < rows) or
                not (0 <= c < cols) or
                (r, c) in visited or
                grid[r][c] == 0
            ):
                return

            visited.add((r, c))
            directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                _check_boundary(new_r, new_c)
                _dfs(new_r, new_c)
        
        rows, cols = len(grid), len(grid[0])
        count = 0
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    _dfs(r, c)

        return count

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    count += 4

                    if r > 0 and grid[r - 1][c]:        # these 2 cells (one on top of other) share a common boundary
                        count -= 2

                    if c > 0 and grid[r][c - 1]:        # these 2 cells (one left to other) share a common boundary
                        count -=2

        return count