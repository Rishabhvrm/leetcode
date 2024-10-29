from typing import List
class Solution:
    '''
    Brute force
    start from every cell in the first column
    standing at a cell, check the 3 available options
    pick the greatest of available 
        (NOPE, could be the case where the less bigger one return max moves)
    if same, pick the one that returns the max ans from it's children

    go till the last column and start return

    standing at a cell I will ask the next 3 to give me the answer and pick max
    TLE: 810/814 -> solved by adding visited set(), could've added dict for memoization
    TIME: O(m * n)
    SPACE: O(m * n)
    '''
    def maxMoves(self, grid: List[List[int]]) -> int:
        
        def dfs(r, c):
            if (r, c) in visited:
                return 0

            visited.add((r, c))
            max_neighbor = 0
            neighbors = [(r - 1, c + 1), (r, c + 1), (r + 1, c +1)]

            for nr, nc in neighbors:
                if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] > grid[r][c]:
                    max_neighbor = max(max_neighbor, 1 + dfs(nr, nc))

            return max_neighbor

        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        visited = set()
        for r in range(ROWS):
            res = max(res, dfs(r, 0))

        return res