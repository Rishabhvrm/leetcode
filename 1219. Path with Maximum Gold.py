from typing import List


class Solution:
    '''
    Time: O( m * n * 3 ^ G), G: number of gold cells
    Space: O(G)
    '''
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.ROWS, self.COLS = len(grid), len(grid[0])
        self.visited = set()
        self.grid = grid
        self.max_profit = 0

        for r in range(self.ROWS):
            for c in range(self.COLS):
                if grid[r][c] != 0:
                    self.dfs_backtracking(r, c, 0)

        return self.max_profit

    def dfs_backtracking(self, r, c, curr_profit):
        if (r not in range(self.ROWS) or
            c not in range(self.COLS) or
            self.grid[r][c] == 0 or (r,c) in self.visited):
            return

        self.visited.add((r,c))
        curr_profit += self.grid[r][c]
        self.max_profit = max(curr_profit, self.max_profit)

        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        for dr, dc in directions:
            new_row, new_col = r + dr, c + dc
            self.dfs_backtracking(new_row, new_col, curr_profit)
        
        self.visited.remove((r,c))