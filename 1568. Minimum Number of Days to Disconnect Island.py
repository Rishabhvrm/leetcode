from typing import List

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def _dfs(r, c, visited):
            if (
                not(0 <= r < rows) or
                not(0 <= c < cols) or
                grid[r][c] != 1 or
                (r,c) in visited
            ):
                return

            visited.add((r, c))
            neighbors = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            for nr, nc in neighbors:
                _dfs(nr, nc, visited)

        def _count_island():
            visited = set()
            island_count = 0
            for r in range(rows):
                for c in range(cols):
                    if (r,c) not in visited and grid[r][c] == 1:
                        _dfs(r,c,visited)
                        island_count += 1
            return island_count

        # A) first check if island removal is needed or not
        island_count = _count_island()                  
        if island_count == 0 or island_count > 1:       # means no island removal needed, i.e. islands are disconnected or doesn't exist
            return 0

        # B) Try removing one land cell and see if it disconnects the island
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    grid[r][c] = 0                                      # change one land cell to water and check
                    island_count = _count_island()
                    if island_count == 0 or island_count > 1:           # means islands are now disconnected or doesn't exist
                        return 1                                        # 1 island removal needed
                    grid[r][c] = 1                                      # revert the change    
            
        # C) by elimination, if above 2 possibilities didn't work, 2 must be the answer
        return 2                                                        
